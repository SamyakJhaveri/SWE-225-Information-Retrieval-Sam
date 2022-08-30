# SWE-225-Information-Retreival-Web-Crawler
Files and instructions about Web Crawler Project built as a capstone of the SWE Information Retrieval Course of Winter 2022 Quarter at UCI taken by Prof. Pramit Choudhary

# Navigating to the Web Crawler Code
The final version of the Web Crawler code can be found in the the "Assignments > Assignment 3 Milestone 3" file path. This also has the final documents and screenshots of what the final result was obtained and eventually submitted as the capstone project for this course. 


Course and Assignment Instructions:
# SWE-225-Web-Crawler
This assignment is to be done in groups of up to 4 students (_you are encouraged to do this assignment in a group!_). You can use a text-processing code that you or any teammate wrote for the previous assignment. You cannot use a crawler code written by non-group-member classmates. Use code found over the Internet at your own peril -- it may not do exactly what the assignment requests. If you do end up using code you find on the Internet, you must disclose the origin of the code.  **As stated in the course policy document, concealing the origin of a piece of code is plagiarism**. Use Ed Discussions for general discussions that can benefit you and everyone.

-------------------------------------------------------------------------------------------------------------------------

In this project, you are going to implement the core of a Web crawler, and then you are going to crawl the  **following URLs (to be considered as domains for the purposes of this assignment) and paths:**

-   *.ics.uci.edu/*
-   *.cs.uci.edu/*
-   *.informatics.uci.edu/*
-   *.stat.uci.edu/*
-   today.uci.edu/department/information_computer_sciences/*

As a concrete deliverable of this project, besides the code itself, you must submit a report containing answers to the following questions:

1.  How many  _unique pages_ did you find?  **Uniqueness for the purposes of this assignment is ONLY established by the URL, but discarding the fragment part.**  So, for example,  _http://www.ics.uci.edu#aaa_  and  _http://www.ics.uci.edu#bbb_  are the same URL. Even if you implement additional methods for textual similarity detection, please keep considering the above definition of unique pages for the purposes of counting the  _unique pages_  in this assignment.
2.  What is the longest page in terms of the number of words? (_HTML markup doesn’t count as words_)
3.  What are the 50 most common words in the entire set of pages  crawled under these domains? (**Ignore English stop words**, which can be found, for example,  [here (Links to an external site.)](https://www.ranks.nl/stopwords)) Submit the list of common words ordered by frequency.
4.  How many subdomains did you find in the ics.uci.edu domain? Submit the list of subdomains ordered alphabetically and the number of unique pages detected in each subdomain. The content of this list should be lines containing  _subdomain_**,** _number,_ for example:  
    vision.ics.uci.edu, 10 (not the actual number here)

**What to submit**: a zip file containing your modified crawler code and the report.

**Grader meetings**: this project requires a meeting of all members of your group with the TAs/Readers, where all of you will be asked questions about your crawler -- your code and the operation of the crawler. These meetings will occur a few days after the submission deadline. Instructions will be sent at the time.

### Specifications

To get started, fork or get the crawler code from  [https://github.com/Mondego/spacetime-crawler4py (Links to an external site.)](https://github.com/Mondego/spacetime-crawler4py)

Read the instructions in the README.md file up to, and including the section "Execution". This is enough to implement the simple crawler for this project. In short, this is the minimum amount of work that you need to do:

1.  Install the dependencies
2.  Set the USERAGENT variable in Config.ini so that it contains all  **students' IDs separated by a comma (the numbers! e.g.** IR CSIF22 UCI-123, 321, 213, 231**)**  of the group members, and  **please also modify the quarter information**  (i.e.  _INF225/CS221_ for Winter 2022).  If you fail to do this properly, your crawler will  **not**  exist in the server's log, which will put your grade for this project at risk.
3.  (**This is the meat of the crawler**) Implement the scraper function in scraper.py. The scraper function receives a URL and corresponding Web response (for example, the first one will be "http://www.ics.uci.edu" and the Web response will contain the page itself). Your task is to parse the Web response, extract enough information from the page (_if it's a valid page_) to be able to answer the questions for the report, and finally, return the list of URLs "scrapped" from that page. Some important notes:
    1.  **Make sure to return only URLs that are within the domains and paths mentioned above**! (see  **is_valid**function in scraper.py -- you need to change it)
    2.  Make sure to defragment the URLs, i.e. remove the fragment part.
    3.  You can use whatever libraries make your life easier to parse things. Optional dependencies you might want to look at: BeautifulSoup, lxml (nudge, nudge, wink, wink!)
    4.  Optionally, in the scraper function, you can also save the URL and the web page on your local disk.
    5.  See  [Crawler Details](https://canvas.eee.uci.edu/courses/42989/pages/crawler-details "Crawler Details")
4.  Run the crawler from your laptop/desktop or from an **ICS openlab machine (**  you can use either the classical ssh&scp to openlab.ics.uci.edu or you can use the web interface hub.ics.uci.edu from your browser; I would recommend you to use ssh, such that you will learn a skill that will be probably important for the rest of your professional life... note that to install any software in machines that you do not own or that you are authorized to sudo, you need to install them to your user folder, and in pip/pip3 you need to use the  --user option to do so**).**  Note that this will take several hours, possibly a day! It may even never end if you are not careful with your implementation! Note that you need to be inside the campus network, or you won't be able to crawl. If your computer is outside UCI, use the VPN.
5.  **Monitor what your crawler is doing**. If you see it trapped in a Web trap, or malfunctioning in any way, stop it, fix the problem in the code, and restart it. Sometimes, you may need to restart from scratch. In that case, delete the frontier file (frontier.shelve), or move it to a backup location, before restarting the crawler.

### Crawler Behavior Requirements

In this project. we are looking for  **text**  in Web pages so that we can search it later on. The following is a list of what a "correct crawl" entails in this context:

-   Honor the politeness delay for each site
-   Crawl all pages with high textual information content
-   Detect and avoid infinite traps
-   Detect and avoid sets of similar pages with no information
-   Detect and avoid dead URLs that return a 200 status but no data ([click here to see what the different HTTP status codes mean (Links to an external site.)](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html))
-   Detect and avoid crawling very large files, if they have low information value

For most of these requirements, the only way you can detect these problems is by first monitoring where your crawler is going, and then adjusting its behavior in order to stay away from problematic pages.

### Test Period and Deployment Period

Due to the nature of this project, the time allocated to it is divided into two parts:

**Test:**  **until February 11th, 9:00pm.** During this time, your crawler can make all sorts of mistakes -- try to crawl outside allowed domains, be impolite, etc. No penalties if you are figuring things out; but penalties if you knock down the server on purpose (i.e.  _removing_  politeness delays). Do not wait until the last minute to start working on your assignment; this assignment requires you to experiment significantly, and you will probably not have time to finish it if you start it late.

**Deployment:** **from February 12th, 9:00am until February 18th, 11:59pm**. This is the real crawl. During this time, your crawler is expected to behave correctly.  **Even if you finish your project earlier, you must operate your crawler during this time period, but you must not restart the crawl more than three times during this period** (unless there is a server issue;  _note that they are all recorded)_.  **You must submit your assignment on Canvas by the due date/time.**

**Late assignments:** For late assignments, you  **cannot**  disrespect the crawling policy during the normal deployment period (_you can only crawl three times during deployment, no more! **MAKE SURE TO DEVELOP AND TEST YOUR CRAWLER DURING THE TEST PERIOD**_). Then you can have from February 19th, 9:00am until February 23rd, 9:00pm as an additional Test period, and from February 24th, 9:00am until February 25, 11:59 pm as an additional Deployment period.  **You need to submit your late assignment in Canvas with an automatic penalty of 25% of the grade by the deadline, and**  **no submission will be accepted after February 25th, not even for reduced points.**

**Note:** The cache server may die for a few hours during these periods due to loads created by impolite crawlers. We will be monitoring closely the server, and it will be back online after (at most)  **~8h hours during the Test period, and after (at most) ~4h during the Deployment period (unless it happens to die during the night - 10:00pm-7:00am)**.  **Make sure to abide by politeness rules and respect your colleagues, especially if you are trying to implement a multithreaded crawler.**

### Extra credit:

**(+2 points)** Implement exact and near webpage similarity detection using the methods discussed in the lecture.  _Your implementation must be made from scratch, no libraries are allowed._

**(+5 points)**  Make the crawler multithread. However, your multithread crawler MUST obey the politeness rule:  **two or more requests to the same domain, possibly from separate threads, must have a delay of 500ms** (this is more tricky than it seems!). In order to do this part of the extra credit, you should read the "Architecture" section of the README.md file. Basically, to make a multithreaded crawler you will need to:

1.  Reimplement the Frontier so that it's thread-safe and so that it makes politeness per domain easy to manage
    
2.  Reimplement the Worker thread so that it's politeness-safe
    
3.  Set the THREADCOUNT variable in Config.ini to whatever number of threads you want
    
4.  **If your multithreaded crawler is knocking down the server you may be penalized**, so make sure you keep it polite (and note that it makes no sense to use a too large number of threads due to the politeness rule that you  **MUST**  obey).

### Grading criteria

1.  Are the analytics in your report within the expected range? (10%)
2.  Did your crawler operate correctly? -- we'll check our logs (~45%)
    1.  Does it exist in Prof. Lopes' Web cache server logs? (**if it's not in the ICS logs, it didn't happen: you will get 0**)
    2.  Was it polite? (penalties for impolite crawlers)
    3.  Did you crawl ALL domains and paths mentioned in the spec? (penalties for missing domains and paths)
    4.  Did it crawl ONLY the domains and paths mentioned in the spec? (penalties for attempts to crawl outside)
    5.  Did it avoid traps? (penalties for falling in traps)
    6.  Did it avoid sets of pages with low information value? (penalties for crawling useless families of pages -  **you must decide and discuss within your group on a reasonable definition for a low information value page and be able to defend it during the interview with the Reader/TAs**)
3.  **Are you able to answer and justify the questions about your code and the operation of your crawler**? (~45%)

### Technical Details

In order not to disrupt the ICS network, your crawlers use a Web cache that is specifically designed for this project, and that runs on one of Prof. Crista Lopes servers. The following picture illustrates the architecture of this project:

![Architecture of Web Crawling Project.png](https://canvas.eee.uci.edu/courses/42989/files/16976546/preview)

If you use the crawler code properly, the cache is largely invisible to you. But you should be aware that it is there. At certain points, you may receive errors that are specifically sent by the cache server to your crawler, when your crawler is doing something it shouldn't -- they are in the 600 range of the status code.  **DO NOT ATTEMPT TO BYPASS THE CACHE!**  -- that may seriously disrupt the ICS network, which may pose additional problems during this already complex quarter.

## Rubric

HW 2 Rubric

HW 2 Rubric

Criteria

Ratings

Pts

This criterion is linked to a Learning OutcomeGroup Grade: Code + Report + Review of the Logs

55  pts  

This criterion is linked to a Learning OutcomeIndividual Grade: Interview

40  pts  

Total Points:  95

