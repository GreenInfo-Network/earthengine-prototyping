### Description

Some early R&D into using Google Earth Engine to do some calculations and work. The ultimate idea would be to replicate something on the order of www.BayAreaGreenPrint.org which handles 20 polygon layers plus a 30-variable "fishnet" point file.

Specific goals:
* Create parameters for project management, in regards to how clients would sign up for GEE accounts as their storage is generous yet not unlimited
* Set up a Linux server with the GEE API for Python
* Load some datasets into a GEE account
* Create some prototyping code that will extract a polygon shape from a shapefile, and perform calculations against the GEE datasets
  * list of distinct area names (city, countty, planning project, fire risk, ...)
  * "fishnet" calculations as used in BAGP: AVG, SUM, MIN, MAX of values found within the area **without** fetching the list of millions of actual values


### Project Status

Timeline was January-February 2018.

After a few weeks of getting to work with it a bit, we will not be using it for calculations such as at BAGP.

* Even simple arithmnetic operations using the `ee.Number` class are "just plain weird" For acreage calculations etc. they are wholly unreliable.
* Calculations such as intersecting area, are also known to be dependent on having a visible GEE map on the screen and using that map's zoom level. Calculation operations without a map are not supported, and give really bizarre answers e.g. acreage.
* Queries for data would be done in a batch mode, in which case the operations could each take a few minutes and will be completed some other time. Our programming paradigm would be to submit these tasks, then keep a list of till-outstanding tasks, gather them on some schedule, and eventually note that all 40+ tasks have completed. Once this is noted, then that cronjob may assemble the report and email the client to come pick it up. This would be an undesirable user experience, as well as infeasibly complex programming for our budgets and timelines.
* Such queries don't support multiple aggregates, so that would be 40+ tasks. Contrast with PostGIS in which we fetch 45 variables in one query, then add 20 more variables from additional datasets.
* API for querying intersecting features is not defined, and G staff could not clarify. Common need is to find not intersecting area or to generate tiles, but to get a distinct list of intersecting items (e.g. names of policy areas).


### GEE API Library & Docs

Noted in the GEE API Github: **The API is in active development, and users should expect the API to change. When (not if) API changes occur, applications that use the API will likely need to be updated.**

Noted: Python for 64-bit Windows doesn't work well, and it is recommended not to use it https://groups.google.com/forum/#!msg/google-earth-engine-developers/iq8EPUVI1e8/i3Zf01nMVywJ

https://developers.google.com/earth-engine/

https://github.com/google/earthengine-api

I went with the manual installation here, as opposed to one of the Docker prospects. This was because I don't know Docker, and also to get more at the nuts-and-bolts for the inevitable need for flexibility and operating on disparate systems where Docker may not be an option.
* The manual installation went fine following the directions here: https://developers.google.com/earth-engine/python_install_manual
* Don't forget the section on "Setting Up Authentication Credentials"
  * Note that the API instructions are incorrect on this one, and instead you will run `earthengine authenticate` from CLI.
  * The new process has you visit a website to issue a token. For a real project, this token would be appropriate to log in P drive or 1Password.
  * As noted in the docs, this will write a file `$HOME/.config/earthengine/credentials` which will cause the Python GEE lib to not require further auth.
    * *How would this translate for a web app?* Would we copy the `.config` folder into content into `~www` so it works with the website?
* Note that Django's geospatial components which would likely form our middleware, make use of GDAL/OGR and this must be installed on the platform.
  * Amazon Linux AMI lacks this and requires manual compilation from source. Ubuntu has it in repositories. The GreenInfo AMI 2017 has it already installed.


### Goals and Milestones

- [x] Basic installation and usage of Python API lib
- [ ] Usage of lib by non-shelll user, e.g. user `www-data` in context of web program e.g. Django
- [ ] Find area of a given polygon using GEE
  * Enables potential to reject a polygon over/under a given acreage
- [ ] Basic querying of a polygon against other polygon datasets, to get distinct "name"
  * Can we get distinct values, or must we fetch back all results?
- [ ] Basic querying of a polygon against other polygon datasets, to get acreage e.g. area which is in CPAD or BPAD
  * Projection/SRS requirements? Can we get accurate meters-based results using whatever SRS GEE uses?
  * Can we get sum acreage (aggregate) instead of distinct records?
- [ ] Basic querying of a polygon against fishnet (raster-like points) to get aggregate stats
  * Need aggregate values, not every single point in the resultset. More important here than in prior tests.
  * MIN, MAX, SUM, AVG are aggregates most commonly used
  * Multiple aggregates in one operation? BAGP fetches **43 aggregates in a single SQL query** and doing this as 43 separate GEE operations may have poor performance

### Running the Demos in Django

Our target platform would be Django, and Django's GeoDjango capabilities for unpacking WKT and reading OGR datasources will allow us to compose semi-realistic use cases using our target library.


```
python manage.py runscript demo0 --traceback
python manage.py runscript demo1 --traceback
```
