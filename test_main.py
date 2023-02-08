import pytest

# readCSV() to update below boolean
run_test_payment = True
run_test_channel = False


@pytest.mark.skipif(not run_test_payment, reason="Skip reason here")
class TestPayment:

    def test_payment_transfer_1(self):
        # Selenium Automation logic here
        assert True
    
    def test_payment_transfer_2(self):
        # Selenium Automation logic here
        assert True


@pytest.mark.skipif(not run_test_channel, reason="Skip reason here")
class TestChannel:

    def test_view_statement_1(self):
        # Selenium Automation logic here
        assert False
        
    
    def test_view_statement_2(self):
        # Selenium Automation logic here
        assert False
