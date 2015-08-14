# Gene Sequence Analysis Framework 2.0

This is the official repository for the GSAF Project. The first version of the framework was a demonstrative prototype. However, it had its own inherent drawbacks that hindered it's efficacy as an effective application framework. These drawbacks include:

## * Ability to process only manually crafted data.
>The dataset cleaning processing involved in the first version of the framework could only function if certain unwanted symbols were removed using external tools and scripts(also coded by me). 

## * Client side data chunking and distribution. 
>Client application was responsible for breaking the dataset into chunks for parallel analysis using the cluster. This meant, that the client had to remain alive for long duration of execution times to get back the graph data structure for post-analysis tasks. Such an assumption is fallacious given that analysis of the dataset requires an execution time that would almost always surpass an acceptable waiting time for a client. 


### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact