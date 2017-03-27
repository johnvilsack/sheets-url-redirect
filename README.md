Google Sheets as URL Redirector
===================

URL redirection link manager for Nginx that uses Google Sheets as a front end interface.

> **Features**

> - Redirect generation can be handled with confidence by non-technicals
> - Sheet provides basic validation of URLs
> - Google Sheets provides easy-to-use versioning to protect your data
> - Script parsing is __FAST__
> - Error correction protects existing "known good" from faults
> - Native nginx redirection; No reliance on databases or dynamic code to parse requests
> - Simple codebase to allow for modification

> **How the Sheet Works:**

> - Add category, name, URL you want, and what it redirects to
> - Spreadsheet will check for basic parsing issues automatically

> **How the Server Works**:

> - Run or cron **make.sh**
> - Creates a CSV from Google Docs using wget
> - Validates CSV to prevent incorrect configurations
> - Creates nginx syntax file of all redirects as redirect.conf
> - Generates static HTML file with list of current redirects for indexing (with additional info)
> - Restarts Nginx server to activate new links

----------

Configure Scripts
-------------

**The Sheet**
1. Clone the Google Sheet using [this template](https://goo.gl/1UYKjZ)
2. Click the blue share button, then "Get Shareable Link"
3. Copy the link it provides
4.  Replace "/edit?usp=sharing" with "/export?format=csv" this is the link needed for make.sh

**The Scripts**
2. Clone this repo "git clone https://github.com/johnvilsack/sheets-url-redirect.git"
3. Find the @@ notations in make.py and make.sh; inserting your customizations

Configure nginx
-------------

In the server{} config:

```
location @redirect {
    include path_to_redirect.conf_file;
}
```
The redirect.conf file will be generated in the same folder you run the script from.

Putting it all together
-------------

1. Run **./make.sh**
2. Test
3. Spend your time on something you enjoy

You can add this to cron for fun and profit.

----------
