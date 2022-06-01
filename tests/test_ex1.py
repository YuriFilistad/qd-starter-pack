from src.ex1 import get_day

def test_get_day():
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday", "Sunday"]
    for i in range(len(days)):
        assert get_day(i+1) == days[i]

