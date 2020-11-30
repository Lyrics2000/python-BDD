from behave import given , when , then


@given('I create a new User')
def create_new_user(context):
    """
    step to create new user
    return    
    """
    print("I am creating new user")
    
@when("I type email")
def type_the_email(context):
    pass