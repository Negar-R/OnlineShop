# Online Shop

> Electronic Commerce is process of doing business through computer networks. A person sitting on his chair in front of a computer can access all the facilities of the Internet to buy or sell the products. Unlike traditional commerce that is carried out physically with effort of a person to go & get products, ecommerce has made it easier for human to reduce physical work and to save time. The main advantage of e-commerce over traditional commerce is the user can browse online shops, compare prices and order merchandise sitting at home on their PC.

> The integration of information and communications technology in business has revolutionized relationships within organizations and those between and among organizations and individuals. Specifically, the use of internet in business has enhanced productivity, encouraged greater customer participation, and enabled mass customization, besides reducing costs.

> Electronic commerce, commonly written as e-commerce, is the trading or facilitation of trading in products or services using computer networks, such as the Internet.

## Purpose of system

The Onlineshop is a virtual store on the Internet where customers can browse the catalog and select products of interest. The selected items may be collected in a shopping cart. At checkout time, the items in the shopping cart will be presented as an order. At that time, more information will be needed to complete the transaction. Usually, the customer will be asked to fill or select a billing address, a shipping address, a shipping option, and payment information such as a credit card number.

The Onlineshop is expanded permanently through new products and services to offer a product portfolio corresponding to the market. Private customers and business customers can order the selected products of the Online service online quickly and comfortably.

## Setup project locally

[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.2-brightgreen.svg)](https://djangoproject.com)
[![Django Rest Version](https://img.shields.io/badge/djangorest-3.11-brightgreen.svg)](https://www.django-rest-framework.org)

First, clone the repository to your local machine:

```
git clone https://github.com/Negar-R/Online_Shop
cd Online_shop
```

To install dependencies in and activate it run the below commands:

```
pipenv install
pipenv shell
```

Create the database by:

```
python manage.py makemigrations
python manage.py migrate
```

To run the project:

```
python manage.py runserver
```
The project will be available at **127.0.0.1:8000**

## URL's introduction

URL | Description
--- | ---
``127.0.0.1:8000/menu`` | In this url you can see online shop's items in multiple category such as : Refrigerator , Mobile , Book and etc.This is the only endpoint that is not necessary to register and it is public.
``127.0.0.1:8000/signup`` | To purchase products from online shop web site , you should register first.After that we send you a verification email and you should verify it to redirect to `login` page.So please enter a valid email !!
``127.0.0.1:8000/edit_prifile`` | For sending items , we need some information about you.e.g : address , phone , ... So please fill provided field in this url.
``127.0.0.1:8000/edit_prifile/my_shopping_cart`` | All items that you added to your shopping cart , is here and you can see them.
``127.0.0.1:8000/edit_prifile/my_paymented_items`` | You can see items that payed for them , here.
``127.0.0.1:8000/finance/MyShoppingCart`` | You can select your needful items and specify their quantities.
``127.0.0.1:8000/finance/MyOrders`` | You can see all items that are in your shopping cart and if you want to pay for them , you should accept them separately.Then they've been provided for pay.
``127.0.0.1:8000/finance/Payment`` | In this url you can select your desire address and pay for items.
``127.0.0.1:8000/suppliar`` | Just admin can access this section and can accept bought items and send them to contributed part.



