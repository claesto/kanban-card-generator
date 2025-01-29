[![Unlicense License][license-shield]][license-url]

# Python Kanban card generator

## About The Project
Managing pantry inventory effectively has always been a challenge, so I explored ways to streamline the process. Inspired by Kanban systems commonly used in just-in-time (JIT) manufacturing and warehouse management, I decided to adapt the concept for personal use.

To achieve this, I developed a macOS and iOS Shortcut that allows items to be added to a list with ease. Using Python and a variety of libraries, I designed a business card-sized Kanban card that can be attached to inventory items. The card features key details, including the product type, manufacturer, store of purchase, Kanban levels, and the quantity to reorder.

A QR code, generated with the Segno library, is prominently displayed on the card. This QR code integrates seamlessly with the Shortcut, enabling quick addition of items to a designated list, such as a grocery list. The result is a compact, efficient, and visually intuitive system for inventory management.

### Built With

* [![Python][Python]][Python-url]
* [![Segno][Segno]][Segno-url]
* [![ReportLab][ReportLab]][ReportLab-url]

## Getting Started

### Prerequisites

Python3 should be installed.

For MacOS & iOS you'd need this shortcut:

1. [AddToList](https://www.icloud.com/shortcuts/609528f7b75b441bb34834c92f07b175)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/claesto/kanban-card-generator.git
   ```
2. Naviate to the repository folder
   ```sh
   cd ...
   ```
3. Create the virtual environment
   ```sh
   python3 -m venv venv
   ```
4. Activate the virtual environment
   ```sh
   source venv/bin/activate
   ```
5. Install required libraries
   ```sh
   venv/bin/python -m pip install -r requirements.txt
   ```
6. Create a Python file or modify the `kanbancard.py` file to create an instance of the class and create a Kanban card.

## Usage

Example on how to create a Kanban card.

1. **Default list name** _(Groceries)_
   ```python
   kbcard = KanbanCard("Product", "Brand", "Supplier", 2, 5)
   ```
2. **Custom list name**
   ```python
   kbcard = KanbanCard("Product", "Brand", "Supplier", 2, 5, list_name="Random list")
   ```

1. `2` is the kanban level
2. `5` is the quantity to purchase

I also included a `generate_cards.py` file to showcase how you'd use this class to generate multiple cards for different products.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the Unlicense License. See `LICENSE.txt` for more information.

## Contact

Tom Claessens - [@claesto](https://twitter.com/claesto) - [Buy me a coffee](https://paypal.me/tomclaessens)

Project Link: [https://github.com/claesto/kanban-card-generator](https://github.com/claesto/kanban-card-generator)


[license-shield]: https://img.shields.io/github/license/claesto/kanban-card-generator.svg?style=for-the-badge
[license-url]: https://github.com/claesto/kanban-card-generator/blob/master/LICENSE.txt

[Python]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Segno]: https://img.shields.io/badge/segno-000000?style=for-the-badge&logo=python&logoColor=white
[Segno-url]: https://pypi.org/project/segno/
[ReportLab]: https://img.shields.io/badge/reportlab-000000?style=for-the-badge&logo=python&logoColor=white
[ReportLab-url]:https://pypi.org/project/reportlab/