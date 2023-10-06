# Mini_test
A repository for an online assessment.

Currently, the repository contains solutions to two problems, FooBar, and Weather forecasting.

## Building and Running
To build and run, clone this repository:
```
git clone https://github.com/BlazedEngima/Mini_test.git
```

Make sure that you have python installed. If not you can download it from [here](https://www.python.org/downloads/).
Download the required packages:
```
pip install -r requirements.txt
```

Then you just need to `cd` into the problem directory of your choice and run the `.py` file
```
cd foo_bar
py foo_bar.py
```
or 
```
cd weather
py weather.py
```
> **_NOTE:_** To run `weather.py`, you need an api key for openweathermap.org. You can either set this api key as an os environment variable (add it to path) or create a seperate `config.py` file and define your api key there.
