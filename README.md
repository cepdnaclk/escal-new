# ESCAL Website

## Table of Contents

- [Under the Hood](#under-the-hood)
- [What is ESCAL](#what-is-escal)
- [New contributor guide](#✨new-contributor-guide)
    - [Getting started](#getting-started)
    - [Using VSCode to build and run the site locally](#using-vscode-to-build-and-run-the-site-locally)
    - [How to contribute](#how-to-contribute)
    - [Website structure](#website-structure)
    - [Folder structure](#folder-structure)
    - [Resources for learning Jekyll](#resources-for-learning-jekyll)
- [TO-DO](#to-do)
    - [Jekyll Templates](#jekyll-templates)
    - [Other](#other)

## Under the Hood

This is the code repository of the new static website made with [Jekyll](https://jekyllrb.com/), for the Embedded Systems and Computer Architecture Laboratory maintained by Department of Computer Engineering, University of Peradeniya, Sri Lanka.

Old website: [https://escal.ce.pdn.ac.lk/](https://escal.ce.pdn.ac.lk/)

## What is ESCAL?

The Embedded Systems and Computer Architecture Laboratory (ESCAL) is a research group at the Department of Computer Engineering at the University of Peradeniya. The primary focus of the group is inclined towards micro-architectural design aspects of embedded microprocessors and their security and reliability concerns.

The group is led by Roshan Ragel and has continued collaborations with Professor Sri Parameswaran at the Embedded Systems Lab, School of Computer Science and Engineering, the University of New South Wales (UNSW), Sydney.

The group consists of the academic staff members of the Department of Computer Engineering, the Postgraduate (Ph.D., M.Phil., M.Eng., and M.Sc.) students from both the Department of Computer Engineering and the Postgraduate Institute of Science (PGIS), and the Undergraduate students from the Department of Computer Engineering and the Department of Statistics and Computer Science. The group also collaborates with the academic staff members, postdoctoral researchers and postgraduate students from the School of Computer Science and Engineering, UNSW. Roshan Ragel regularly visits UNSW, Sydney, as a visiting research fellow.

At present, the group works on the following themes:

- Security and Reliability of Embedded Systems
- Side-Channel Attacks and Countermeasures
- Application Specific Processor and Memory Hierarchy Design
- High-Performance Computing

## ✨New contributor guide

If you're a new contributor, please follow the following guidelines.

### Getting Started

To get started, follow the following steps:

1. **Clone the repository** to your local machine
```bash
$ git clone https://github.com/cepdnaclk/escal-new.git
```

2. **Install Jekyll**. You have two options:
    - [Follow the Jekyll installation instructions](https://jekyllrb.com/docs/#instructions). These steps will guide you through installing Ruby and Jekyll locally.
    - Use [the anaconda distrubution](https://conda.io/) and [conda-forge](https://conda-forge.org/).
    First, install [miniconda](https://conda.io/miniconda.html) or [anaconda](https://www.anaconda.com/download/). Then run the following command:
    ```bash
    $ conda install -c conda-forge ruby c-compiler compilers cxx-compiler
    ```
    Finally, install Jekyll and Bundler, which will let you install the dependencies for the site:
    ```bash
    $ gem install jekyll bundler
    ```

3. **Install the site's build dependencies**. These are specified in ```Gemfile```. From the root of the repository, run:
```bash
$ bundle install
```
This step might take a few moments as it must download and install a number of local extensions. It will create a local file called Gemfile.lock. These are the "frozen" dependencies and their version numbers needed to build the site.

4. **Build the site locally**. From the root of the repository, run:
```bash
$ bundle exec jekyll serve liveserve
```
This will build the site's HTML and open a server at localhost:4000 for you to preview the site.

### Using VSCode to build and run the site locally

We recommend using VSCode to build and run the site locally since it is very convenient. To do so, follow the following steps:

1. Install [Jekyll Run](https://marketplace.visualstudio.com/items?itemName=Dedsec727.jekyll-run) extension on VSCode.
2. After installing the extension, open VSCode settings (Preferences > Settings) and search for ```Jekyll-run```. Then, find the **Command Line Arguments** section and add the following arguments:
```bash
--livereload --force_polling --port 3000
```
3. Now, you can build and run the site locally by clicking the play button with ```Jekyll Run``` label on the bottom left corner of VSCode. Note that this extension will also automatically install the required dependencies.

### How to contribute

You must push your changes to the ```gh_pages_dev``` branch and create a pull request to the ```main``` branch. [@NuwanJ](https://github.com/NuwanJ), [@Akilax0](https://github.com/Akilax0), [@sathiiii](https://github.com/sathiiii), [@shamalweerasooriya](https://github.com/shamalweerasooriya), or [@dinuransika](https://github.com/dinuransika) will review your pull request and merge it to the ```main``` branch. Please do test your changes locally before creating a pull request. Also, link the issue you're working on in the pull request.

### Website structure

Please refer to [this](https://docs.google.com/document/d/1DQfEFddiAAaibxmIE9xFhlh3L8IREGh1tpRZav_g_ms/edit#heading=h.88al9ys3mfrf) document for the website structure.

### Folder structure

All the folders that has a name starting with ```_``` are used by Jekyll to build the website. Please refer to [this](https://jekyllrb.com/docs/structure/) document for more information.

#### ```.github/workflows```

This folder contains the GitHub Actions workflow files. Currently, there is only one workflow file called ```scheduled-deploy.yml```. This workflow file is used to deploy the website to the ```main``` branch every Sunday at 12:00 AM (00:00) GMT+5:30. It basically runs the python scripts to generate the static pages and pushes them to the ```main``` branch. The commit will trigger the GitHub Pages build process and the website will be updated.

#### ```assets```

This folder contains the assets used in the website including css, js, images, and fonts. If you want to add new styles, please edit the ```assets/css/style.css``` file. Try to use Bootstrap4.0 styles as much as possible. Refer to the [Bootstrap 4.0 official documentation](https://getbootstrap.com/docs/4.0/getting-started/introduction/) for more details. If you want to add new JavaScript scripts, please edit the ```assets/js/scripts.js``` file.

#### ```pages```

This folder contains all the HTML pages of the website. The pages that are generated from the python scripts are located here. If you want to add a new page, please create a folder with the page name and add an ```index.html``` file to it. If there're subpages, add them to the same folder as well.

#### ```python_scripts```

This folder contains the python scripts used to pull data and generate HTML pages. If you want to add a new script, please add it to this folder.

### Resources for learning Jekyll

- [Jekyll official documentation](https://jekyllrb.com/docs/)
- [Running Jekyll](https://learn.cloudcannon.com/jekyll/running-jekyll/)
- [Jekyll file structure](https://learn.cloudcannon.com/jekyll/jekyll-file-structure/)
- [Introduction to Liquid](https://learn.cloudcannon.com/jekyll/introduction-to-liquid/)
- [Liquid documentation](https://shopify.github.io/liquid/)
- [Introduction to front matter](https://learn.cloudcannon.com/jekyll/introduction-to-jekyll-front-matter/)
- [Introduction to layouts](https://learn.cloudcannon.com/jekyll/introduction-to-jekyll-layouts/)
- [Introduction to includes](https://learn.cloudcannon.com/jekyll/introduction-to-jekyll-includes/)
- [Control flow in Liquid](https://learn.cloudcannon.com/jekyll/control-flow-statements-in-liquid/)
- [String filters in Liquid](https://learn.cloudcannon.com/jekyll/string-filters-in-liquid/)
- [Looping in Liquid](https://learn.cloudcannon.com/jekyll/looping-in-liquid/)
- [Introduction to collections](https://learn.cloudcannon.com/jekyll/introduction-to-jekyll-collections/)
- [Introduction to data files](https://learn.cloudcannon.com/jekyll/introduction-to-jekyll-data-files/)
- [Introduction to permalinks](https://learn.cloudcannon.com/jekyll/introduction-to-jekyll-permalinks/)

## TO-DO

### Jekyll Templates

- [x] Template for main site.
- [x] Dynamic navigation bar.
- [x] Template for Projects page.
- [x] Template for People page.
- [ ] Template for ESCAL Bio-med page.
- [X] Template for ESCAL Robotics page.
- [ ] Template for ESCAL GPU page.
- [ ] Template for Resources page.

### Other

- [x] Python script to extract and save information of ESCAL related people from the API.
- [x] Python script to extract and save ESCAL related project information from the API.
- [x] Add pagination to the projects page.
- [x] Pages for all project categories.
- [x] Implement projects search.
- [x] Project thumbnails (For now: placeholders).
- [ ] Implement theme switcher.
- [ ] Implement people page.
- [ ] Implement Research home page.
- [ ] Implement Resources page -> Create cards for ESCAL facilities (robotics, wearables, fpgas, etc.)
- [x] Improve footer.
- [ ] Re-organize the home page layout -> Add latest project updates in the hero section, recent projects, recent works, etc.
- [ ] Prepare a site plan (user navigation diagram kind of thing, with all the possible pages).
- [ ] Improve pagination controls in the Projects page.
- [ ] Implement the filtering functionality of the tag cloud in the Projects page.
- [ ] Add project tags to the project extraction script.
