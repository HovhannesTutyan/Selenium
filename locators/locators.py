from selenium.webdriver.common.by import By

class homePageLocators:
    _login_button={"by":By.XPATH, "value":"/html/body/div[1]/header/div[2]/a[3]"}
    _start_now={"by":By.XPATH,"value":"/html/body/div[1]/header/div[2]/a[2]"}
    _cincopa_home={"by":By.XPATH,"value":"/html/body/div[1]/header/div[1]/div[1]/a/img"}
    _products_home={"by":By.XPATH,"value":"/html/body/div[1]/header/nav/ul/li[1]/a"}
    _solutions_home={"by":By.XPATH,"value":"/html/body/div[1]/header/nav/ul/li[2]/a"}
    _resources_home={"by":By.XPATH,"value":"/html/body/div[1]/header/nav/ul/li[3]/a"}
    _pricing_home={"by":By.XPATH,"value":"/html/body/div[1]/header/nav/ul/li[4]/a"}

class LoginPageLocators:
    _home_button={"by":By.XPATH,"value":"/html/body/div[1]/header/div[1]/div[1]/a/img"}
    _username_input={"by":By.ID,"value":"email"}
    _password_input={"by":By.ID,"value":"password"}
    _signin_button={"by":By.ID,"value":"submitBtn"}
    _signin_saml={"by":By.LINK_TEXT,"value":"Sign in with SAML SSO"}
    _forgot_password={"by":By.LINK_TEXT,"value":"Forgot your password?"}
    _create_account={"by":By.LINK_TEXT,"value":"Create one"}

class NavigationLocators:
    _open_gallery={"by":By.XPATH,"value":"/html/body/div[1]/div[1]/ul/li[1]/a"}
    _open_assets={"by":By.XPATH,"value":"/html/body/div[1]/div[1]/ul/li[2]/a"}
    _open_analytics={"by":By.XPATH,"value":"/html/body/div[1]/div[1]/ul/li[3]/a"}
    _open_dashboard={"by":By.XPATH,"value":"/html/body/div[1]/div[1]/ul/li[4]/a"}
    _product_changes={"by":By.XPATH,"value":"/html/body/div[1]/div[1]/div[2]/ul[1]/li[1]/a/i"}
    _create_new_gallery_button={"by":By.XPATH,"value":"/html/body/div[1]/div[1]/div[2]/ul[3]/li/div"}
    _create_new_gallery_hover={"by":By.XPATH,"value":"/html/body/div[1]/div[1]/div[2]/ul[3]/li/div/div/i"}
    _create_new_gallery_hover_template={"by":By.XPATH,"value":"/html/body/div[1]/div[1]/div[2]/ul[3]/li/div/div/ul/li[2]/a"}
    _create_new_gallery_hover_empty_gallery={"by":By.XPATH,"value":"/html/body/div[1]/div[1]/div[2]/ul[3]/li/div/div/ul/li[3]/a"}
    _create_new_gallery_hover_asset={"by":By.XPATH,"value":"/html/body/div[1]/div[1]/div[2]/ul[3]/li/div/div/ul/li[4]/a"}
    _upgrade_button={"by":By.XPATH,"value":"/html/body/div[1]/div[1]/div[2]/a"}
    _account_hover={"by":By.XPATH,"value":"/html/body/div[1]/div[1]/div[2]/ul[4]/li/a/i"}
    _account_hover_dashboard={"by":By.LINK_TEXT,"value":"Account Dashboard"}
    _account_hover_switch={"by":By.LINK_TEXT,"value":"Switch Account"}
    _account_hover_change_plan={"by":By.LINK_TEXT,"value":"Change Plan"}
    _account_hover_user_profile = {"by": By.LINK_TEXT, "value": "User Profile"}
    _account_hover_invite_manage = {"by": By.LINK_TEXT, "value": "Invite & manage members"}
    _account_hover_billing = {"by": By.LINK_TEXT, "value": "Billing"}
    _account_hover_integrations = {"by": By.LINK_TEXT, "value": "Integrations"}
    _account_hover_close_captions = {"by": By.LINK_TEXT, "value": "Automatic Closed Captions"}
    _account_hover_product_changes = {"by": By.LINK_TEXT, "value": "Product Changes"}
    _account_hover_logout = {"by": By.LINK_TEXT, "value": "Logout"}

class GalleriesLocators:
    _upload_files={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[2]/div[1]/a[1]"}
    _search_input={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/input"}
    _search_search={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/a[1]/i"}
    _search_delete={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/div[1]/div[2]/div/a[2]"}
    _galleries_sort_options={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/div[1]/div[4]/div[1]/div"}
    _galleries_sort_by_last_change={"by":By.XPATH,"value":"/html/body/form/div[3]/div[2]/div[3]/div[1]/div[4]/div[1]/ul/li[1]/a"}
    _galleries_sort_by_traffic={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/div[1]/div[4]/div[1]/ul/li[2]/a"}
    _galleries_sort_by_view={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/div[1]/div[4]/div[1]/ul/li[3]/a"}
    _galleries_view_options={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/div[1]/div[4]/div[2]/div/a"}
    _galleries_view_normal={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/div[1]/div[4]/div[2]/div/a"}
    _galleries_view_grid={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/div[1]/div[4]/div[2]/ul/li[2]/a"}
    _galleri_title_edit={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[4]/td[2]/span/a"}
    _galleri_title_input={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[4]/td[2]/div[1]/form/input"}
    _galleri_title_input_confirm={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[4]/td[2]/div[1]/form/div/a[1]"}
    _galleri_title_input_cancel={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[2]/div[1]/form/div/a[2]"}
    _galleri_desc_edit={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[4]/td[2]/div[3]/a"}
    _galleri_desc_input={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[4]/td[2]/div[4]/textarea"}
    _galleri_desc_confirm={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[4]/td[2]/div[4]/div/a[1]"}
    _galleri_desc_cancel={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[4]/td[2]/div[4]/div/a[2]"}
    _customize_galleri={"by":By.XPATH,"value":"/html/body/form/div[3]/div[2]/div[3]/table/tbody/tr[4]/td[1]/div[2]/a[1]"}
    _manage_galleri={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[4]/td[1]/div[2]/a[2]"}
    _embed_galleri={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[4]/td[1]/div[2]/a[3]"}
    _more_actions={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[4]/td[1]/div[2]/a[4]"}
    _more_actions_duplicate={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[4]/td[1]/div[2]/div/div/ul/li[1]"}
    _more_actions_reorder={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[4]/td[1]/div[2]/div/div/ul/li[2]"}
    _more_actions_download={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[1]/div[2]/div/div/ul/li[5]"}
    _more_actions_delete={"by":By.LINK_TEXT,"value":"Delete gallery"}
    _gallery_tag={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[4]/td[2]/div[7]/a"}
    _gallery_tag_input={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[4]/td[2]/div[7]/div[2]/div[1]/div"}
    _confirm_tag_input={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[4]/td[2]/div[7]/div[2]/div[1]/div/p/span[2]"}
    _gallery_tag_input_apply={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[4]/td[2]/div[7]/div[2]/div[2]/a"}
    _gallery_items_manage={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[1]/td[3]/div/div[2]"}
    _gallery_items_manage_checkbox={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[2]/td/div[2]/div[1]/div[1]/div/label/i"}
    _remove_selected={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[2]/td/div[2]/div[1]/div[1]/button[1]/b"}
    _delete_selected={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[2]/td/div[2]/div[1]/div[1]/button[2]/b"}
    _gallery_items_item_checkbox={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[2]/td/div[2]/div[2]/ul/li[1]/div[1]/label/i"}
    _gallery_items_item_view={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[2]/td/div[2]/div[2]/ul/li[1]/div[3]/a"}
    _gallery_items_item_download={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[2]/td/div[2]/div[2]/ul/li[1]/div[4]/a[1]"}
    _gallery_items_item_share={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[2]/td/div[2]/div[2]/ul/li[1]/div[4]/a[2]/i"}
    _gallery_items_item_remove={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[2]/td/div[2]/div[2]/ul/li[1]/div[4]/a[3]/i"}
    _gallery_items_add_files={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[2]/td/div[2]/div[1]/a[1]"}
    _gallery_items_open_in_assets={"by":By.XPATH,"value":"/html/body/div[1]/div[2]/div[3]/table/tbody/tr[2]/td/div[2]/div[1]/a[2]"}









