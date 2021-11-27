# Holiday Counter Application
Working Business Days Counter in a given date range, Using the Calendarific API. <br>
Currently tuned to return working days as per the National Holidays in India.

![Working Application Interface](https://github.com/varungupta31/Holiday-Counter-App/blob/main/images/workingIMG.png)

## Note

The calendarific API has not been updated for Python 3, and is likely to result in an attribute error.

```
AttributeError: 'dict' object has no attribute 'has_key'
```

The following patch in suggested for the ```__init__.py```

```

import json
import requests

class v2:
    api_key = None

    def __init__(self, api_key):
        self.api_key = api_key

    def holidays(self, parameters):
        url = 'https://calendarific.com/api/v2/holidays?'

        if not 'api_key' in parameters :
            parameters['api_key'] = self.api_key

        response = requests.get(url, params=parameters);
        data     = json.loads(response.text)

        if response.status_code != 200:
            if not 'error' in data is False:
                data['error'] = 'Unknown error.'

        return data
```   
