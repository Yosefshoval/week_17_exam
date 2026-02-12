from fastapi import APIRouter

router = APIRouter()

@router.get('/analytics/top-customers')
def top_customers():
    pass


@router.get('/analytics/customers-without-orders')
def customers_without_orders():
    pass


@router.get('/analytics/zero-credit-active-customers')
def zero_credit_active_customers():
    pass
