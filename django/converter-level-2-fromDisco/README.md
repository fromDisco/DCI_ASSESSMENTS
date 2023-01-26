Design a django project called "mediamarkt" with only one application called: `customers`.

You are requested to add a `custom path converter` that checks for a valid German number.

The url you will design should support the following examples:

Order of difficulty has been placed side by side:

Easy - `http://localhost:8000/customers/phone/+491739561284/`

Easy - `http://localhost:8000/customers/phone/(+49) 1798341284/`

Medium - `http://localhost:8000/customers/phone/+49 19 39 35 12 84/`

Hard - `http://localhost:8000/customers/phone/+49 (1788) 34 12 84/`

Hard - `http://localhost:8000/customers/phone/+49 (1781) 34-56-84/`


The minimum to pass is to validate all the Easy use cases.
If a number is invalid, a 404 page will be rendered automatically (you can ignore invalid phones).
The urls shared are a simplified version of the URL. In reality, spaces are represented differently when typed in a url. 

We call this URL encoding, learn more about it here: https://www.w3schools.com/tags/ref_urlencode.ASP

No models are required in this exercise. Only views and templates will be programmed.

# Setup instructions

- Create a virtual env
- Install the requirements (right now it is just Django)

In the customers application, create a view function that sends back a template with the following words:

```
Your phone number: +491739341284 is valid

Ihre Rufnummer: +491739341284 ist gültig
```

Please note that phone numbers like `+491739341284` have been hardcoded here, you will be expected to pass this phone number to the template dynamically as context variable for example - `render(request, <'some template.html'>, <{ a dictionary with your variables }>)`.

Your converter may use regular expressions or string methods you think are appropriate to check for valid numbers.

## Resources

- https://www.lebara.com.au/how-to-call-germany-phone-numbers 
- https://allaboutberlin.com/guides/dial-phone-numbers-germany
- https://en.wikipedia.org/wiki/Telephone_numbers_in_Germany

