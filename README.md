# 🎨 drf-material

**drf-material** is a project that gives a sleek and elegant look to the browsable API of Django REST Framework using Material Design.

We want to make the API more **appealing** and **intuitive** for developers and users alike.
That's why we created a **beautiful** and **responsive** design that follows the Material Design principles and guidelines.

Our goal with drf-material is to make your work easier and faster when working with Django REST Framework.
We think that by improving the user experience, we can help you create stunning and powerful web applications.

So if you're looking for a better way to work with Django REST Framework, don't hesitate to try drf-material.
We're sure you'll be impressed by it as much as we are!

## 🌟 Features

- **Modern design**: drf-material uses Material Design, a design system based on Google's Material Design and
  Bootstrap's components, to create a sleek and elegant design for the API.
- **Accessibility**: drf-material follows the best practices for web accessibility,
  ensuring that the API is easy to use for everyone, regardless of their abilities or preferences.
- **Form input max length indicators**: drf-material shows the maximum length of each form input field,
  so you know how much data you can enter. The indicators also change color when you reach the limit, giving you visual feedback.
- **Form inputs required indicators**: drf-material marks the required form input fields with an asterisk (*),
  so you know which fields are mandatory to submit the form. The indicators also show an error message if you try to submit the form without filling the required fields.
- **Browser form validation**: drf-material uses the built-in browser form validation features, such as HTML5 attributes
  to validate the form input data before sending it to the server. The validation checks for data types, formats, patterns, ranges, and more.

## 🛠️ Get started

To use drf-material, follow these simple steps:

- Install the package:

```console
pip install drf-material
```

- Add `drf_material` to `INSTALLED_APPS` setting, before `rest_framework`

```python
# settings.py

INSTALLED_APPS = [
    ...
    'drf_material',
    'rest_framework',
    ...
]
```

That's it! You're ready to go. 😎

I hope you find this useful. Let me know if you have any feedback or questions. 😊
