# FontCut
API that cuts fonts based on text. By now it just supports woff fonts

## Install for Mac

```bash
make setup
```

## Run for Mac

```bash
make run
```

## Install and Run for Ubuntu like

* Install dependencies from requirements.apt
* Override PYTHONPATH:

```bash
export PYTHONPATH=$PYTHONPATH:/usr/lib/python2.7/dist-packages/site-packages/
```

* Use Procfile to run project


## Using Project

* Run API

* Send post request to / with a JSON like this:

```bash
{
"text": "A",
"font_url": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.6.3/fonts/fontawesome-webfont.woff"
}
```

* Now you have base64 font for letter A
