from Pensieve.old.engines import Engine, OpenAI

API_KEY = "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"

SYSTEM_PROMPT = \
    """
A university has developed a system to detect plagiarism by students. After submitting an essay, students are asked 
interview style questions by a tutor about the content of their essay. You are a component of this system, tasked with generating the questions.
You will be provided with only the student submitted essay as a user input.
For the essay, generate 5 suitable questions. Questions should be numbered 1 through 5.
For each question generate a sample answer with reference to the essay with the line and column number of the place in 
the essay you are referencing. Where multiple answers may be considered correct, provide multiple sample answers. 

Each answer should begin with the phrase "Sample Answer: ", and references should be formatted "(Reference: ...)" and include quotes where possible.
"""

ESSAY_TEXT = """
Sydney Transport Social Distancing
System Design Document
Report By:
Luke Glover
45965587
Client Representative:
Connor Lines
45214832
Table of Contents
Revision History .............................................................................................................................. 3
1. System Design Document ............................................................................................................... 4
1.1 System Architecture ............................................................................................................ 4
1.2 File and Database Design .................................................................................................... 5
1.3 Package Diagram ................................................................................................................. 6
1.4 Design Class Diagram .......................................................................................................... 7
1.5 State Diagram...................................................................................................................... 8
2. Data Definitions .............................................................................................................................. 9
3. Requirements Traceability Matrix .................................................................................................. 9
4. Test Specification .......................................................................................................................... 11
4.1 Overview ........................................................................................................................... 11
4.2 Test Cases.......................................................................................................................... 12
4.3 Test Plan ............................................................................................................................ 14
5. Report ........................................................................................................................................... 16
Vision Statement
This project aims to facilitate the increasing usage of our public transport system, as COVID-19
restrictions are eased throughout Sydney, in a manner that minimises the possibility of disease
transmission. Following the advice of NSW Health, Transport for New South Wales is enforcing social
distancing on board buses, trains, ferries, and all other modes of transport in the network. However,
enforcement of social distancing rules is difficult, and the client is seeking to develop an automated
system to aid customers and staff in making transport COVID-Safe.
Revision History
Date Changes
16 / 10 / 2020 Initial document structure drafted. Vision statement written.
23 / 10 / 2020 System architecture, database design, data definitions and package layout
drafted.
25 / 10 / 2020 Class diagram and state diagram drafted.
26 / 10 / 2020 Test cases designed and included.
27 / 10 / 2020 Test specification and test plan outlined.
28 / 10 / 2020 Document layout and sections finalised. Spelling and grammar check.
Supporting Documents and References
‘COMP2050_SHFYR_2020_ALL_U: Assignments 1 and 2: Project A’. Available online:
https://ilearn.mq.edu.au/mod/page/view.php?id=5911581
‘COMP2050_SHFYR_2020_ALL_U: Assignment 2: Further notes on system design documents’.
Available online: https://ilearn.mq.edu.au/mod/page/view.php?id=5911576 (accessed Oct. 28,
2020).
‘COMP2050_SHFYR_2020_ALL_U: Assignment 2: Further notes on testing documentation’. Available
online: https://ilearn.mq.edu.au/mod/page/view.php?id=6054106
‘Sydney Transport Social Distancing Initiative - Software Requirements Specifications’. Connor Lines.
1. System Design Document
1.1 System Architecture
The system consists of three distinct subsystems: display devices, sensing devices and a central
server. The software component of the display devices and sensing devices, collectively referred to
as client devices, will be built following a pipe and filter architecture. The system as whole is
modelled as a client-server architecture.
The system will consist of many client devices, that are installed across the TfNSW and a central
server responsible for coordinating and controlling the clients. There are two types of client device
that fulfill one of two roles: display or capacity sensing. This design decision is based on
requirements R20 and R23.
Client Device Hardware
The display devices will consist of a Raspberry Pi Zero W single board computer, with a lithium ion
battery, screen, and speaker, housed in a plastic case. The sensing devices will similarly include a
Raspberry Pi Zero W, lithium ion battery and plastic case, but a Raspberry Pi High Quality Camera in
place of a display and speaker. These hardware components were chosen with consideration of
requirements R8, R9, R10 and R11.
The Raspberry Pi Zero W is a commercially available, extremely cost effective (R20) and power
efficient single board Linux based computer, with relatively powerful compute capabilities, and
extensive I/O support, including USB, HDMI, and Ethernet and a number of wireless technologies.
This is the obvious choice over a custom hardware solution, which would add unnecessary cost and
complexity for minimal benefit. In addition, because the Raspberry Pi Zero W runs a Linux based
operating system, the software project can take advantage of existing display, audio, camera, and
network drivers, reducing the complexity of the project and reducing development time. The
Raspberry Pi High Quality Camera is a first party add-on for the Raspberry Pi Zero W, and is similarly
cost effective, and integrates extremely easily, with drivers and software libraries being made
available by the Raspberry Pi Foundation
The decision to build two separate, battery powered devices for display and sensing was guided by
requirements R18, R20, R23 and R25. The need to develop distinct solutions for different mode of
public transport is eliminated, reducing complexity, cost, and time to availability, potentially at a
slight expense to the efficiency of the complete system (more devices places more load on the
network and the server). The need to recharge batteries is also an inconvenience, however, since it
is predicted the system will be retired after the threat of COVID-19 has passed, the additional
installation time that would be required to integrate the devices into the electrical systems of
vehicles was deemed to be wasteful.
Display and Sensing Device Software
Software for both devices will be written in the Python programming language, because of good
support for Linux environments and the extensive Python Standard Library provides well tested,
efficient code for several of the most common functions, including graphics and networking.
The display device software will contain two modules: a networking module, responsible for
handling communication with the server; and a display module, responsible for drawing the user
interface and the received data onto the screen.
The sensing device will feature three modules: a camera module, responsible for the collection of
images from the camera; a classification module that counts the passengers in the vehicles; and a
networking module, similar to that of the display device, that is responsible for communication with
the server. Of particular interest is the classification module. This module will consist of a
Tensorflow Lite object detection model, trained using Google Cloud’s AutoML service.
Server Hardware and Software
The central server will be several virtual machines, hosted on Compute Engine, the Infrastructure as
a Service component of the Google Cloud Platform. This service allows automatic scaling of virtual
infrastructure to meet demand, as well as automatic load balancing. Compute Engine is similarly
priced to Amazon’s EC2 service and Microsoft’s Azure service; however, it is comparatively much
simpler, which improves to the time to availability for the system.
The software component of the server will also be written in Python, using the Flask web
framework. The server communicates with the client devices over HTTPS, with data in the JSON
format.
1.2 File and Database Design
See also: Section 2. Data Definitions
The data that is collected and processed by this system will be in the JSON format, due to
widespread support for the format in existing software libraries, including the Python Standard
Library. Data will be stored in a document storage database, rather than a table database. This
reduces development times since code does not have to be written to convert data from JSON
format to a column format.
Cloud Firestore is a flexible and massively scalable NoSQL database solution provided by the Google
Cloud Platform, supporting real time updating and offline usage. In Cloud Firestore, documents
contain named fields, which in turn store values, and fields can be nested in other fields. Similar or
related documents, in turn, are grouped into collections. Google provided libraries allow the
documents to be represented by Python language dictionaries, making it trivial to convert between
JSON strings and Firestore Documents.
1.3 Package Diagram
1.4 Design Class Diagram
1.5 State Diagram
The Server.Manager class has a complex set of states and interactions, which are described in the
following state diagram:
2. Data Definitions
This section describes data as it appears in the class diagram (section 1.4, above).
Field Type Meaning Example
DataPoint.timestamp Datetime.datetime The timestamp that the
DataPoint was generated
(2020, 10, 28, 17,
0, 0)
Zone.zoneID integer The unique identifier for a
zone
1
Zone.capacity integer The number of passengers
allowed to be riding in the
zone
60
Zone.occupancy integer The number of passengers
currently riding in the zone
45
Vehicle.vehicleID string The TfNSW identifier for the
vehicle
AB1234
Vehicle.location tuple(float, float) Longitude and latitude of the
vehicle
(-33.777041,
151.118023)
Vehicle.routeDistance float The percentage of the route
length the vehicle has
covered
0.12
Route.routeID string TfNSW provided route
“number”
178X
Route.path list(tuple(float,float)) A list of tuples containing
latitude and longitude of
points along the route
(-33.777041,
151.118023),
(-33.778833,
151.173219),
(-33.778833,
151.173219)
3. Requirements Traceability Matrix
Req.
ID
Use Cases Packages Classes Methods Build
No.
R1 Enter Zone /
Exit Zone
Client.Sensing.Camera
Client.Sensing.Classifier
Camera
Classifier
captureImage()
makeClassification()
R2 Direct Passenger
Elsewhere
Shared.Types DataPoint (Requirement
satisfied by fields)
R3 Direct Passenger
Elsewhere /
Change Occupancy
Count
Shared.Types DataPoint (Requirement
satisfied by fields)
R4 Change Occupancy
Count
Shared.Types DataPoint getPercentFilled()
R5 Change Occupancy
Count
Shared.Types DataPoint (Requirement
satisfied by fields)
R6 Direct Passenger
Elsewhere
Shared.Types DataPoint (Requirement
satisfied by fields)
R7 Change Occupancy
Count
Shared.Types DataPoint (Requirement
satisfied by fields)
R8 Hardware requirement
R9 Direct Passenger
Elsewhere
Client.Display
Client.Display
Graphics
Audio
paint()
playSound()
R10 Direct Passenger
Elsewhere
Client.Display Graphics paint()
R11 Direct Passenger
Elsewhere
Client.Display Graphics paint()
R12 Hardware requirement
R13
R14
R15
R16
R17
R18
R19
R20
Non-functional requirement
R21
R22
Hardware requirement
R23
R24
R25
Non-functional requirement
R26 Direct Passenger
Elsewhere
Client.Display Graphics paint()
4. Test Specification
4.1 Overview
The following test cases and test plan are designed to test for compliance with the following
functional requirements:
- R2: Each zone must have a designated passenger count
- R3: Each zone must have a static designated maximum occupancy as per COVID-19
regulations
- R4: The system must be able to compare the passenger count with the maximum occupancy
- R5: The system must be able to track passengers across every zone in each train
- R6: The system must have a location value for each zone
- R7: The system must have the passenger count, maximum occupancy, and location of each
zone always stored and available for use
- R9: If there are seats available in a zone, the display must automatically inform passengers
of how many seats the zone has available
- R10: If there are no seats available in the current zone, the display must warn passengers
not to enter
- R13: The system must be able to notify nearby transport personnel in case of an error of the
system or a violation of regulations on the part of the passengers
- R14: Transport personnel must be able to override the current passenger count in each zone
In addition, a small set of non-functional requirements are included:
- R19: The system must have complete reliability in passenger tracking
- R24: The system must be able to fulfill the requirements for increasing numbers of
passengers, to and beyond the maximum occupancy capacity for each zone
- R26: The UI must be user-friendly and readily available
Some requirements were excluded for being hardware or installation requirements (e.g. R1, R8, R12)
that are not applicable to this software testing specification or were deemed to be too subjective to
reliably test in a scientific manner (e.g. R11). Tests will also be included to cover requirements not
listed in the Software Requirements Specification, but that were deemed important, such as
performance under heavy load.
Several test types will be implemented to adequately cover the described requirements. These tests
include unit tests to ensure the correct functionality of implemented methods and packages as a
whole, integration tests to test the interactions of modules and the interactions of separate devices,
simulated load testing and stress testing to ensure adequate performance in actual operation.
4.2 Test Cases
Test
No.
Requirement Test Description Input Output
T1 R2, R4, R5 Black-box* unit test
This test will ensure
the passenger
detection subsystem
can accurately and
reliable count the
passengers in each
zone, and that the
value correctly
propagates
throughout the
system.
The input for this test
case is a live image. To
manipulate the value,
volunteers enter or
leave the zone. The
following counts will be
tested:
- 0 (empty)
- 1
- 15 (half full)
- 30 (at capacity)
- 35 (above capacity)
The expected output is
the correct value for
the number of
volunteers in the zone.
A count 1 below or
above the true value is
considered acceptable,
except in the case of an
empty zone, where 0
must be returned.
T2 R3, R4, R6,
R7
White-box unit test
This test will ensure
that the correct values
for several parameters
are set, and these
values propagate
throughout the system
without error. It also
tests that the system
correctly produces
errors if configuration
is incorrect
The input for this test
case consists of system
configurations. The
following settings for
capacity will be tested:
- 0 (no passengers
allowed)
- 30 (actual capacity)
- 100 (unreasonably
high)
- -1 (invalid value)
The system should
accept values 0, 30,
100, and these values
should be reflected in
the internal state of the
system. Value -1 should
cause an error.
T3 R9, R10, R13 Integration Test
This test ensures that
information correctly
flows from sensing
devices, to the server,
then to display
devices. This means a
relevant and accurate
message is displayed
on screens when the
zone is in a variety of
states. It will also test
the alert system that
notifies TfNSW staff
when COVID-19
guidelines are
breached.
The input for this test is
the number of
passengers in each
zone. Volunteers will
not be used for this test,
and instead the input
will be simulated, using
the images that were
recorded in test T1. The
following values will be
tested:
- 0 (empty)
- 1
- 15 (half full)
- 30 (at capacity)
- 35 (above capacity)
The expected output is
shown on the display
devices. In cases 0, 1,
and 15, the display
should instruct
passengers to enter the
zone. In case 30, it
should inform
passengers of the
nearest zone with
capacity. In case 35, the
display should instruct
passengers to leave,
and the system should
inform TfNSW staff.
Test
No.
Requirement Test Description Input Output
T4 R13, R14,
R26
White-box unit test
and Integration Test
This test ensures that
the online access
panel available to
TfNSW staff is
correctly
implemented, and the
prescribed training is
adequate for TfNSW
to use the system.
TfNSW staff will receive
basic training on the
web interface, then will
required to carry out
several actions. The
tasks they will complete
include:
- Receiving and alert
from the system
- Dismissing the alert
- Manually overriding
capacity limits
- Reverting override
back to actual value
There are two ‘outputs’
that will be monitored
during this test.
Developers will monitor
the internal state of the
system and ensure that
the changes made by
TfNSW staff are
reflected, and training
personnel will ensure
that the TfNSW are
able to correctly carry
out their tasks.
T5 R19, R24 White-box Load
Testing
This test is designed to
ensure the server
hardware and
software can scale to
meet the expected
demand before the
complete system is
implemented.
Both the system’s
internal API and the
web interface will be
placed under a
simulated load of
approximately 5,000
requests per minute.
This value is based on
the number of services
offered by TfNSW in
Sydney.
The load on the server
will be monitored
throughout the test, as
well as the average
response time (time to
first byte). The
response time should
not exceed 100ms.
T6 R19, R24 Black-box** stress
testing
This test will ensure
the system is able to
recover from unusual
or unexpected events.
The server will be
loaded as with test T4,
however, the rate of
requests will grow until
the system fails.
The system is not
expected to continue
responding to requests
during the simulated
load. Once the load is
removed, the system is
expected to make a
graceful recovery.
T7 R19, R24 Black-box** stress
testing
This tests will ensure
unrelated components
continue operating in
the event of a fatal
error in the system.
The system will operate
as normal until the
server is terminated by
engineers.
Client devices must
continue operating,
displaying an error
message where
possible (display
devices), or silently
continuing (sensing
devices).
* This test is described as “black box” because the internal state of the TensorFlow Lite model is not
accessible.
** These tests are black box tests due to the difficulty of monitoring the internal state of the entire
system during operation
4.3 Test Plan
4.3.1 Test Environment
These tests will be conducted in a controlled environment. The server will be a full-scale
implementation, whilst only a small number of client devices will be implemented on vehicles
designated for testing purposes. These vehicles will be a combination of buses, trains, metro trains
and ferries that are currently out of service (i.e. not currently transporting passengers).
Test T1 is a potentially dangerous test. Volunteers will be required to temporarily breach COVID-19
restrictions to ensure the system reacts appropriately. To mitigate the risks, all volunteers will be
required to wear masks, and the test duration will be as short as possible. The images recorded by
sensing devices during test T1 will be reused for test T3, so that volunteers are not required to
conduct this test.
4.3.2 Test Modes
Tests T1 and T2 will be automated tests that are run following any changes to the relevant
components of the system. Of particular importance, test T1 must be rerun when the Tensorflow
Lite model is updated, as regression due to poor quality training is a major concern for machine
learning models.
Test T4 will involve TfNSW staff, attempting to complete predetermined tasks after receiving basic
training in usage of the system. Whilst the users are completing the tasks, engineers will monitor the
internal state of the components of the system to ensure the tasks are correctly being processed by
the system.
Tests T3, T5, T6 and T7 will be manually undertaken, as these processes would be difficult to
automate and careful monitoring of the system would be required.
4.3.3 Documentation
Instruction manuals and other training materials for the web interface must be produced before
tests involving volunteers and TfNSW staff. This is of particular importance for test T1, which is
potentially hazardous. Strict COVID safety protocols must be developed and adhered to.
Following testing, a large number of log files, system dumps and measurements will be made
available to developers to identify and resolve issues with the system/
4.3.4 Test Procedures
Logging
Each client device and server involved in the test will log any anomalous behaviour in log files. This
includes, but is not limited to, runtime errors, unexpectedly slow operations, and temperature and
power supply issues. In addition, the web interface server will produce an access log of all incoming
connections during the test period. In addition, all requests made and all responses received by the
client devices will be logged to local storage and recovered following the completion of the test, to
identify where in the system errors occur if they occur.
Set-up
Before the running of each test, the system is reset to a default state. This is to prevent any potential
errors during a test to interfere with the results of subsequent tests. A variety of valid configuration
files are to be made available during the testing process.
Tests T2, T4, T5 are conducted with the relevant component running under the GNU Project
Debugger (GDB). Breakpoints are to be placed before and after the execution of the relevant
sections of code, so that compliance with pre- and post-conditions can be verified.
Start-up and proceeding
Except when a specific test (e.g. T2) requires non-standard configuration, valid configuration files are
loaded into the system. The test is performed as described in section 4.2. For tests T3, T4, T5 and T6
the complete system is operating during the duration of the test, unless the system encounters a
fatal error. For tests T1 and T2, only the relevant component of the system should be operating, and
any required network activity should be simulated.
Measurement
For tests running under GDB (T1, T2), at each breakpoint, the complete internal state of the system
is dumped for future analysis. This allows developers to ensure the internal state reflects the
changes being made to the system during the test.
For test T3, engineers will manually monitor the display devices and ensure the displayed values are
accurate. Except the standard logs described above, no extra measurements will be made.
For load and stress tests(T4, T5), the response time is measures as the time interval, in milliseconds,
between a client device issuing a request and the client device receiving the first byte of the
response. The time to download is defined as the time between receiving the first byte of a response
and receiving the last byte of the response. In addition, the per core, per thread and total CPU
utilisation of the relevant servers will be recorded in 1 second intervals. Logs, as described above will
be created by every device involved in the test and recovered from the interna storage of the device.
In the event of a system failure, a complete system dump will be recorded for future analysis.
Shut down, stopping, and restarting
After the completion of a test, the system is stopped according to standard operating procedures.
The server software is stopped at the command line, and server logs are copied off the machine
using SFTP before the server is shut down. Client devices simply have their battery removed. The
internal storage is removed from each client device and logs are downloaded to development
machines.
Contingencies
In the event of an anomalous behaviour, the test should continue. This will provide useful
information on the propagation of errors through the system, and the impacts of incorrect data on
the system. The test should be repeated once the source of the anomalous behaviour has been
identified and corrected.
In the event of a fatal error, the affected components of the system should dump their internal
state. Devices or components not affected by the error, may exhibit reduced functionality, but must
NOT crash or shutdown until manually terminated. Tests should be repeated when the source of the
fatal error is identified.
5. Report
This project was an interesting one to work on. The design of software is a challenging topic, with
many angles to consider.
The SRS I was provided did not include fit criteria, which caused some difficulties in designing tests
for those requirements. To overcome this, I carefully considered the requirements instead, and
designed tests that would ensure the requirements were met without making use of fit criteria. In
addition, the report I was given was missing a few section entirely, but I was able to resolve this by
messaging my partner, who was quick to reply and send me the sections I needed.
My largest problem with this assignment was this very section, which was missing from the version
uploaded to iLearn, and only included with very minimal time to spare.
"""

def generate():

    print("Generating questions...")

    engine: Engine = OpenAI(API_KEY)

    engine.system(SYSTEM_PROMPT)
    engine.user(ESSAY_TEXT)

    completion = engine.complete()

    return completion["choices"][0]["message"]["content"]

