from fastapi import APIRouter

router = APIRouter()


# GET ALL PRODUCTS
@router.get("/")
def get_products():

    return {
        "success": True,
        "products": [

            {
                "category": "Loans",
                "items": [
                    "Home Loan",
                    "Personal Loan",
                    "Business Loan",
                    "Education Loan",
                    "Loan Against Property",
                    "Car Loan",
                    "Gold Loan",
                    "Cash Credit & Overdraft"
                ]
            },

            {
                "category": "Insurance",
                "items": [
                    "Life Insurance",
                    "Health Insurance",
                    "Term Insurance",
                    "Motor Insurance",
                    "Travel Insurance",
                    "Business Insurance"
                ]
            },

            {
                "category": "Mutual Funds",
                "items": [
                    "SIP Investment",
                    "Tax Saving Investment",
                    "Wealth Management",
                    "Mutual Fund Services"
                ]
            }

        ]
    }