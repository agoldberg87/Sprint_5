class Locators:

    # Кнопки
    login_and_register_button = ".//button[text()='Вход и регистрация']"
    no_account_button = ".//button[text()='Нет аккаунта']"
    login_button = ".//button[text()='Войти']"
    register_button = ".//button[text()='Создать аккаунт']"
    logout_button = ".//button[text()='Выйти']"
    place_ad_button = ".//button[text()='Разместить объявление']"
    place_ad_button_class = "buttonPrimary inButtonText undefined inButtonText"
    submit_ad_button = ".//button[text()='Опубликовать']"
    user_avatar = ".//button[@class='circleSmall']"
    right_button = ".//button[@class='arrowButton arrowButton--right undefined']"

    # Для рандомного выбора
    category_dropdown_button = ".//div[@class='dropDownMenu_dropMenu__sBxhz'][.//input[@name='category']]//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']"
    category_options = ".//div[@class='dropDownMenu_dropMenu__sBxhz'][.//input[@name='category']]//div[@class='dropDownMenu_hidden__qBq1t']/button"
    
    city_dropdown_button = ".//div[@class='dropDownMenu_dropMenu__sBxhz'][.//input[@name='city']]//button[@class='dropDownMenu_arrowDown__pfGL1 dropDownMenu_noDefault__wSKsP']"
    city_options = ".//div[@class='dropDownMenu_dropMenu__sBxhz'][.//input[@name='city']]//div[@class='dropDownMenu_hidden__qBq1t']/button"

    condition_radio_buttons = ".//div[@class='createListing_inputRadio__ApFGD']"

    # Поля
    email_field = ".//input[@name='email']"
    password_field = ".//input[@name='password']"
    repeat_password_field = ".//input[@name='submitPassword']"
    ad_name_field = ".//input[@name='name']"
    ad_description_field = ".//textarea[@name='description']"
    ad_price_field = ".//input[@name='price']"

    # Прочие элементы
    user_name = ".//h3[@class='profileText name']"

    error_notice = ".//span[text()='Ошибка']"
    authorization_notice = ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']"
    
    input_parent = ".//input[@name='email']/parent::div[@class='input_inputError__fLUP9']"

    profile_header = ".//h1[text()='Мой профиль']"
    ad_card = ".//div[@class='profilePage_gridAndPaginaton__togPs']//div[@class='card'][last()]//h2"

    # Креды
    login_email = "13571357@test.ru"
    login_password = "11335577"