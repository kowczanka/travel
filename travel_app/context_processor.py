from datetime import datetime

def date(request):
    return {'date': datetime.now().date()}