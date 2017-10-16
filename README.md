# Threads vs. Processes

A proof of concept for computationally intensive thread vs. process benchmark. 

### Description

An experiment involving the use of the Python language and the multiprocessing and threading libraries was done in order to measure the efficiency and performance of using multiple processes versus multiple threads. The experiment tested a computation where the program generated a large random number with both threads and processes. Each test used 5 processes or 5 threads to complete the computation. Each was timed and measured how fast each thread or process completed.
A computationally intensive task (one that tested CPU performance) was better suited to be done with multiple processes, as the average runtime for multiple processes was 2.273929 with an upper bound of roughly 2.5 seconds. The threading program running the same test, but with threads, reported an average runtime of 6.751263 seconds with each thread completing sequentially and having an upper bound of roughly 10 seconds.

### Installation / Usage

Clone the repository and install the required python packages:

```
python install -r requirements.txt
```
 
Run the python scripts `thread-test.py` or `process-test.py` to test threads or processes respectively.

### Discoveries

The problem we are trying to solve is to measure the performance and efficiency of using multiple threads versus multiple processes. We will be using Python as the language of choice with use of the multiprocessing and threading modules. Each module will be separated into their own program and execute a mathematically intensive computation. Since we are dealing with CPU performance, I chose to execute a computationally intensive problem over an I/O intensive problem. CPU bound operations are more easily recoverable from intensive workloads than File I/O intensive workloads. This program is designed to be as lightweight as possible while still being a good test case.

#### Multiprocessing
Multiprocessing and the idea of running computations in parallel has grown rapidly in recent years. As more and more CPU manufacturers add cores to their products, application programmers are seeing opportunities to increase performance and efficiency by running computations in parallel where applicable. Multiprocessing also does not share the same memory space between processes, and so does not need any locking mechanism to prevent two different processes writing to the same memory space and potentially causing havoc. Spawning processes also takes more time and consumes a larger memory footprint than using threads.
The multiprocessing module in Python offers a number of ways to run workloads in parallel. The Process, Queue, and Lock classes are available to influence how the CPU distributes the workload amongst its available cores. In our experiment, the Process class is the method of choice as we simply want to spawn a number of processes to handle the workload.

#### Threading
Threading is the idea that processes share the same core and the same memory space, but are quicker to spawn than processes and allow data to be shared between threads. This allows for a number of benefits such as being able to reliably depend on the system to allocate resources in sequence to a program running in a thread.
In threading, there is a mechanism known as the GIL, or the Global Interpreter Lock. This mechanism ensures that CPU time is given in sequence to threads that require it at any given time. This allows the application to be locked from trying to do the same thing at the same time, and effectively ration CPU time between operations as the application switches between threads to complete the task.

#### The Computation
For testing the efficiency and performance of threading versus multiprocessing, I do a simple mathematical operation that generates large numbers. The algorithm I’m using for each individual thread and process is

```
start_num = start_num * randint(1,9) / randint(1,5)) * num_computations
```

Basically I take a starting value and equal it to itself, multiplied a random number between 1 and 9, then divide it by a random number between 1 and 5. Finally, I loop that equation by a number of computations; in this case I loop it 100,000 times. Each time it loops, the start_num value has a value equal to the previous loop. This number has the potential to be very large, and as seen in the output file of each program, it’s several hundred digits large.

### Prerequisites

* Python 2.7+

## Built With

* [Python](https://python.org) - The programming language used

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](tags).

* 1.0.0 - **Initial version** - Pushed to GitHub for public viewing

## Authors

* **Travis Ryder** - *Owner* - [TravisRyder.com](https://travisryder.com)

See also the list of [contributors](graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* BCIT BTech Program