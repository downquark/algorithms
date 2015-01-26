from square_root import sqrt

@given('I have a number, {number}')
def step_impl(context, number):
   context.number = int(number)

@when('I compute the square root')
def step_impl(context):
    context.result = sqrt(context.number)
    
@then('the square root should be returned')
def step_impl(context):
    assert context.number == round(context.result ** 2)
    #'square root is not as expected')