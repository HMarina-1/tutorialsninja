import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


@allure.feature('Menu Navigation')
@allure.suite('Main Menu Tests')
@allure.title('Verify navigation of main menu items')
@allure.description('This test clicks through several main menu items and verifies navigation.')
@allure.severity('normal')
def test_menu_item(driver):
    with allure.step('Navigate to the homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    expected_menu_items = ["Desktops", "Laptops & Notebooks", "Components", "Tablets", "Software", "Phones & PDAs",
                           "Cameras", "MP3 Players"]

    with allure.step('Click on menu item: Desktops'):
        menu_item1 = driver.find_element(By.LINK_TEXT, expected_menu_items[0])
        menu_item1.click()

    with allure.step('Click on menu item: Laptops & Notebooks'):
        menu_item2 = driver.find_element(By.LINK_TEXT, expected_menu_items[1])
        menu_item2.click()

    with allure.step('Click on menu item: Components'):
        menu_item3 = driver.find_element(By.LINK_TEXT, expected_menu_items[2])
        menu_item3.click()

    with allure.step('Click on menu item: Tablets'):
        menu_item4 = driver.find_element(By.LINK_TEXT, expected_menu_items[3])
        menu_item4.click()
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[3]

    with allure.step('Click on menu item: Software'):
        menu_item5 = driver.find_element(By.LINK_TEXT, expected_menu_items[4])
        menu_item5.click()
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[4]

    with allure.step('Click on menu item: Phones & PDAs'):
        menu_item6 = driver.find_element(By.LINK_TEXT, expected_menu_items[5])
        menu_item6.click()
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[5]

    with allure.step('Click on menu item: Cameras'):
        menu_item7 = driver.find_element(By.LINK_TEXT, expected_menu_items[6])
        menu_item7.click()
        assert driver.find_element(By.TAG_NAME, 'h2').text == expected_menu_items[6]

    with allure.step('Click on menu item: MP3 Players'):
        menu_item8 = driver.find_element(By.LINK_TEXT, expected_menu_items[7])
        menu_item8.click()



@pytest.mark.parametrize("menu_locator, submenu_locator,result_text", [
    (
            (By.PARTIAL_LINK_TEXT, "Desktops"),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[1]/a'),
            'PC'
    ),
    (
            (By.PARTIAL_LINK_TEXT, "Desktops"),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[1]/div/div/ul/li[2]/a'),
            'Mac'
    ),
    (
            (By.PARTIAL_LINK_TEXT, "Laptops & Notebooks"),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[1]/a'),
            'Macs'
    ),
    (
            (By.PARTIAL_LINK_TEXT, "Laptops & Notebooks"),
            (By.XPATH, '//*[@id="menu"]/div[2]/ul/li[2]/div/div/ul/li[2]/a'),
            'Windows'
    )
])
@pytest.mark.regression
@allure.feature('Menu Navigation')
@allure.suite('Submenu Selection')
@allure.title('Verify Submenu Navigation')
@allure.description(
    'This test verifies that clicking on submenu items navigates to the correct page and displays the expected header.')
@allure.severity('normal')
def test_tested_menu(driver, menu_locator, submenu_locator, result_text):
    with allure.step('Open the homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step('Locate the menu item'):
        menu = driver.find_element(*menu_locator)

    with allure.step('Locate the submenu item'):
        submenu = driver.find_element(*submenu_locator)

    with allure.step('Hover over the menu and click on the submenu'):
        ActionChains(driver).move_to_element(menu).click(submenu).perform()

    with allure.step('Wait for the header to appear and verify the header text is as expected'):
        header_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, 'h2'))
        )
        assert header_element.text == result_text


@pytest.mark.regression
@allure.feature('Product Search')
@allure.suite('Search Functionality')
@allure.title('Verify Product Search by Name')
@allure.description(
    'This test verifies that the search function returns the correct results when searching for a product by the name "MacBook".'
)
@allure.severity('normal')
def test_search_product(driver):
    with allure.step('Open the homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step('Locate the search field'):
        search = driver.find_element(By.NAME, "search")

    with allure.step('Enter product name into the search field'):
        search.send_keys('MacBook')

    with allure.step('Click the search button'):
        button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.btn-lg')
        button.click()

    with allure.step('Retrieve the list of found products'):
        products = driver.find_elements(By.TAG_NAME, 'h4')

    with allure.step('Filter the found products by name'):
        new_list = [elem.text for elem in products if 'MacBook' in elem.text]

    with allure.step('Verify that all found products contain "MacBook"'):
        assert len(products) == len(new_list), "Some products do not contain 'MacBook'"


@pytest.mark.smoke
@allure.feature('Shopping Cart')
@allure.suite('Add to Cart Functionality')
@allure.title('Verify Product Can Be Added to Cart')
@allure.description('This test verifies that a user can add a product to the cart and check the cart contents.')
@allure.severity('critical')
def test_add_to_cart(driver):
    with allure.step('Open the homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step('Locate the product "MacBook" button'):
        product = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[1]')

    with allure.step('Click the "Add to Cart" button'):
        product.click()

    with allure.step('Wait for success message to be visible'):
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success"))
        )

    with allure.step('Verify the success message contains confirmation'):
        assert "Success: You have added" in success_message.text, "Success message not found."

    with allure.step('Wait until cart total is updated to show 1 item'):
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.ID, "cart-total"), "1 item(s)")
        )

    with allure.step('Click the cart button'):
        cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "cart"))
        )
        cart_button.click()

    with allure.step('Wait for cart contents to be visible'):
        cart_contents = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.dropdown-menu.pull-right"))
        )

    with allure.step('Verify that "MacBook" is in the cart contents'):
        assert "MacBook" in cart_contents.text, f"Expected 'MacBook' in cart, but got: {cart_contents.text}"


@pytest.mark.parametrize("button, header, text", [
    (
        (By.XPATH, '/html/body/footer/div/div/div[1]/ul/li[1]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "About Us"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[1]/ul/li[2]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Delivery Information"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[1]/ul/li[3]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Privacy Policy"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[1]/ul/li[4]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Terms & Conditions"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[2]/ul/li[3]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Site Map"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[3]/ul/li[3]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Affiliate Program"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[3]/ul/li[4]/a'),
        (By.XPATH, '//*[@id="content"]/h2'),
        "Special Offers"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[2]/ul/li[1]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Contact Us"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[2]/ul/li[2]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Product Returns"
    ),
    (
        (By.XPATH, "/html/body/footer/div/div/div[3]/ul/li[1]/a"),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Find Your Favorite Brand"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[3]/ul/li[2]/a'),
        (By.XPATH, '//*[@id="content"]/h1'),
        "Purchase a Gift Certificate"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[4]/ul/li[1]/a'),
        (By.XPATH, '//*[@id="content"]/div/div[1]/div/h2'),
        "New Customer"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[4]/ul/li[2]/a'),
        (By.XPATH, '//*[@id="content"]/div/div[1]/div/h2'),
        "New Customer"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[4]/ul/li[3]/a'),
        (By.XPATH, '//*[@id="content"]/div/div[1]/div/h2'),
        "New Customer"
    ),
    (
        (By.XPATH, '/html/body/footer/div/div/div[4]/ul/li[4]/a'),
        (By.XPATH, '//*[@id="content"]/div/div[1]/div/h2'),
        "New Customer"
    ),
])
@pytest.mark.regression
@allure.feature('Footer Functionality')
@allure.suite('Footer Navigation')
@allure.title('Verify Footer Links Navigate Correctly')
@allure.description('This test checks that footer links navigate to the expected page and display the correct header.')
@allure.severity('normal')
def test_footer(driver, button, header, text):
    with allure.step('Open the homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step('Locate the footer button'):
        footer_button = driver.find_element(*button)

    with allure.step('Click the footer button'):
        footer_button.click()

    with allure.step('Wait for the header text of the new page to be visible'):
        footer_header_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(header)
        ).text

    with allure.step('Verify that the header text is as expected'):
        assert footer_header_text == text, f"Expected text '{text}', but got '{footer_header_text}'"


@pytest.mark.smoke
@pytest.mark.smoke
@allure.feature('Slider Functionality')
@allure.suite('Image Slider')
@allure.title('Verify Slider Navigation')
@allure.description(
    'This test checks the functionality of the image slider, ensuring it navigates between images correctly.')
@allure.severity('normal')
def test_slider_functionality(driver):
    with allure.step('Open the homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step('Locate the slider'):
        slider = driver.find_element(By.CLASS_NAME, 'swiper-container')

    with allure.step('Verify the slider is visible'):
        assert slider.is_displayed(), "Slider is not visible on the page."

    with allure.step('Get the source of the first slide'):
        first_slide = driver.find_element(By.CSS_SELECTOR, '.swiper-slide-active img')
        first_slide_src = first_slide.get_attribute('src')

    with allure.step('Locate the next arrow button'):
        next_arrow = driver.find_element(By.CLASS_NAME, 'swiper-button-next')

    with allure.step('Click the next arrow to navigate to the next slide'):
        ActionChains(driver).move_to_element(slider).click(next_arrow).perform()

    with allure.step('Wait for the slider to move to the next image'):
        WebDriverWait(driver, 20).until_not(
            EC.element_to_be_clickable(first_slide)
        )

    with allure.step('Get the source of the new active slide'):
        new_slide = driver.find_element(By.CSS_SELECTOR, '.swiper-slide-active img')
        new_slide_src = new_slide.get_attribute('src')

    with allure.step('Verify the slider has moved to a new image'):
        assert first_slide_src != new_slide_src, "Slider did not move to the next image."

    with allure.step('Locate the previous arrow button'):
        prev_arrow = driver.find_element(By.CLASS_NAME, 'swiper-button-prev')

    with allure.step('Click the previous arrow to navigate back'):
        prev_arrow.click()

    with allure.step('Wait for the slider to return to the first image'):
        WebDriverWait(driver, 20).until_not(
            EC.element_to_be_clickable(new_slide)
        )

    with allure.step('Get the source of the reverted slide'):
        reverted_slide_src = driver.find_element(By.CSS_SELECTOR, '.swiper-slide-active img').get_attribute('src')

    with allure.step('Verify the slider has returned to the first image'):
        assert reverted_slide_src == first_slide_src, "Slider did not return to the first image."


@pytest.mark.smoke
@allure.feature('Wishlist Functionality')
@allure.suite('User Actions')
@allure.title('Add Product to Wishlist')
@allure.description(
    'This test verifies that a user can successfully add a product to their wishlist and check its contents.')
@allure.severity('normal')

def test_wish_list(driver, login):
    with allure.step('Open the homepage'):
        driver.get("https://tutorialsninja.com/demo/")

    with allure.step('Locate the "Add to Wishlist" button for MacBook'):
        add_elem_wishlist = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[2]')

    with allure.step('Click the "Add to Wishlist" button'):
        add_elem_wishlist.click()

    with allure.step('Wait for the success message to appear'):
        success_message = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-success"))
        )

    with allure.step('Verify the success message is displayed correctly'):
        assert "Success: You have added MacBook to your wish list!" in success_message.text, "The success message did not appear as expected."

    with allure.step('Locate the wishlist total element'):
        wishlist_total = WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable((By.ID, 'wishlist-total'))
        )

    with allure.step('Verify the wishlist total is updated'):
        assert "1" in wishlist_total.text, f"Expected '1' in wishlist total, but got {wishlist_total.text}"
    sleep(2)
    with allure.step('Click on the wishlist total to view contents'):
        wishlist_total.click()

    with allure.step('Wait for the wishlist contents to become visible'):
        wishlist_contents = WebDriverWait(driver, 50).until(
            EC.visibility_of_element_located((By.LINK_TEXT, 'MacBook'))
        )

    with allure.step('Verify that MacBook is present in the wishlist'):
        assert "MacBook" in wishlist_contents.text, "MacBook not found in wishlist"










