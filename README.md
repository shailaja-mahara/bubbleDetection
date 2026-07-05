# Introduction
- Master Thesis
<!-- 
## :ledger: Index

- [About](#beginner-about)
- [Usage](#zap-usage)
  - [Installation](#electric_plug-installation)
  - [Commands](#package-commands)
- [Development](#wrench-development)
  - [Pre-Requisites](#notebook-pre-requisites)
  - [Developmen Environment](#nut_and_bolt-development-environment)
  - [File Structure](#file_folder-file-structure)
  - [Build](#hammer-build)  
  - [Deployment](#rocket-deployment)  
- [Community](#cherry_blossom-community)
  - [Contribution](#fire-contribution)
  - [Branches](#cactus-branches)
  - [Guideline](#exclamation-guideline)  
- [FAQ](#question-faq)
- [Resources](#page_facing_up-resources)
- [Gallery](#camera-gallery)
- [Credit/Acknowledgment](#star2-creditacknowledgment)
- [License](#lock-license) -->

##  :beginner: About
This project is about using an automating the approach to superbubble detection using Convolutional Neural Networks (CNN) deep learning to efficiently detect, superbubbles in astronomical images from the PHANGS-JWST survey.

<!-- ## :zap: Usage
Write about how to use this project.
create a entry script for base execution -->

###  :electric_plug: Installation
- Add Setup and Installations

```
$ add installations steps if you have to.
```

###  :package: Commands
- Add terminal command and entry script command

##  :wrench: Development
Add list of supervisors email/github

### :notebook: Pre-Requisites
List all the pre-requisites the system needs to develop this project.
- A tool

###  :nut_and_bolt: Development Environment
Write about setting up the working environment for your project.
- How to download the project...
- How to install dependencies...


###  :file_folder: File Structure
Add a file structure here with the basic details about files, below is an example.

```bash
├── data
│   ├── patches
│   │   ├── test
│   │   │   ├── images
│   │   │   ├── masks
│   │   ├── train
│   │   │   ├── images
│   │   │   ├── masks
│   │   ├── val
│   │   │   ├── images
│   │   │   ├── masks
│   ├── processed
│   │   ├── images
│   │   ├── masks
│   │   ├── metadata
│   │   ├── patches
│   ├── raw
│   │   ├── catalogue
│   │   ├── fits
├── notebooks
│   ├── data
│   │   ├── processed
│   │   │   ├── patches
├── outputs
│   ├── figures
│   │   │   ├── catalogueA
│   │   │   ├── catalogueB
│   │   │   ├── catalogueC
│   │   │   ├── **/*.png
│   │   │   ├── **/*.pdf
└── .gitignore
└── README.md
```

FInal pipeline to this table
| No | File Name | Details 
|----|------------|-------|
| 1  | index | Entry point

###  :hammer: Build
Entry script command and options

### :rocket: Deployment
Write the deployment instruction here.

## :cherry_blossom: Community

If it's open-source, talk about the community here, ask social media links and other links.

 ###  :fire: Contribution

 Your contributions are always welcome and appreciated. Following are the things you can do to contribute to this project.

 1. **Report a bug** <br>
 If you think you have encountered a bug, and I should know about it, feel free to report it [here]() and I will take care of it.

 2. **Request a feature** <br>
 You can also request for a feature [here](), and if it will viable, it will be picked for development.  

 3. **Create a pull request** <br>
 It can't get better then this, your pull request will be appreciated by the community. You can get started by picking up any open issues from [here]() and make a pull request.

 > If you are new to open-source, make sure to check read more about it [here](https://www.digitalocean.com/community/tutorial_series/an-introduction-to-open-source) and learn more about creating a pull request [here](https://www.digitalocean.com/community/tutorials/how-to-create-a-pull-request-on-github).


 ### :cactus: Branches

 I use an agile continuous integration methodology, so the version is frequently updated and development is really fast.

1. **`stage`** is the development branch.

2. **`master`** is the production branch.

3. No other permanent branches should be created in the main repository, you can create feature branches but they should get merged with the master.

**Steps to work with feature branch**

1. To start working on a new feature, create a new branch prefixed with `feat` and followed by feature name. (ie. `feat-FEATURE-NAME`)
2. Once you are done with your changes, you can raise PR.

**Steps to create a pull request**

1. Make a PR to `stage` branch.
2. Comply with the best practices and guidelines e.g. where the PR concerns visual elements it should have an image showing the effect.
3. It must pass all continuous integration checks and get positive reviews.

After this, changes will be merged.


### :exclamation: Guideline
coding guidelines or other things you want people to follow should follow.


## :question: FAQ
You can optionally add a FAQ section about the project.

##  :page_facing_up: Resources
Add important resources here

##  :camera: Gallery
Pictures of your project.

## :star2: Credit/Acknowledgment
Credit the authors here.

##  :lock: License
Add a license here, or a link to it.