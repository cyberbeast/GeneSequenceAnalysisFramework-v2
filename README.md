# Gene Sequence Analysis Framework 2.0 #

This is the official repository for the GSAF Project. The first version of the framework was a demonstrative prototype. However, it had its own inherent drawbacks that hindered it's efficacy as an effective application framework. These drawbacks include:
* **High data processing and analysis time.**
* **Ability to process only manually crafted data.**
* **Client side data chunking and distribution.**
* **Manual update of Worker Node Task definitions**
* **Heavy File I/O operations.**
* **High error reporting time for Framework Testing.**

*See the section on Description of Drawbacks of GSAF 1.0 for a more verbose explanation of the drawbacks.*

### Description of Drawbacks of GSAF 1.0 ###
* #### High data processing and analysis time ####
>Using the approach that was previously devised for a graph based analysis of gene data required a substantial amount of time for execution. The longest I remember running the program when developing the framework was 4 days before the process (sadly, and unfortunately) revealed an error towards the end.

* #### Ability to process only manually crafted data. ####
>The dataset cleaning processing involved in the first version of the framework could only function if certain unwanted symbols were removed using external tools and scripts(also coded by me). 

* #### Client side data chunking and distribution. ####
>Client application was responsible for breaking the dataset into chunks for parallel analysis using the cluster. This meant, that the client had to remain alive for long duration of execution times to get back the graph data structure for post-analysis tasks. Such an assumption is fallacious given that analysis of the dataset requires an execution time that would almost always surpass an acceptable waiting time for a client. 

* #### Manual update of Worker Node Task definitions ####
>The previous framework required the Worker Node tasks to be copied/loaded manually onto each worker node. This proved to be a huge constraint, as even small code updates to the framework required significant setup time for the framework for test executions. This was quite a hindrance to the development process, because spending time to setup the framework everytime the code needs to be tested/updated was counterproductive.

* #### Heavy File I/O operations ####
>The initial framework used a data structure that I created to hold the results of the graph-based analysis of the dataset. With respect to the amount of computation time that was required for analysis of a chromosome then, file I/O operations did not add to much delay (although it was indeed significant with respect to CPU load). However, with an increase in computation speed and decrease in processing time for each chromosome dataset (due to parallelization), File I/O ended up contributing to almost half the execution time of the primary modules.

* #### High error reporting time for Framework Testing ####
>As mentioned earlier, since the client application had to wait till the entire file is processed and analyzed over the cluster of worker nodes dedicated to this task, when testing different aspects of the code for the framework, a quantitatively large amount of time was required for errors to be reported back to the client (even if the errors were generated at the beginning of the code)


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