# Getting started

## Introduction

Send SMS messages using Unifonic Messaging API. Get your dedicated Universal number, and
start sending messages today.

Unifonic NextGen Restful and HTTP **API's** uses The basic Authentication protocol. All
request and response bodies are formatted in JSON.

## Get an account

To start using the API you need to send an email to Unifonic to create Appsid for you.

## Base URL

All URLs referenced in the documentation have the following base:

**el.cloud.unifonic.com**

## Security

To ensure privacy we recommend you to use HTTPS for all Unifonic API requests. you can
download our HTTPS certificate.

[Download] (https://api.unifonic.com/udm/https.zip)

## Formats

Unifonic API only supports JSON format. All request must use the Content-type header set
to application/json.

## Support

We’re here to help! Get in touch with support at <support@unifonic.com> and we’ll get
back to you as soon as we can or you can contact us throw live chat on our [website]
(www.unifonic.com).

## How to Build

You must have Python `2 >=2.7.9` or Python `3 >=3.4` installed on your system to install
and run this SDK. This SDK package depends on other Python packages like nose,
jsonpickle etc. These dependencies are defined in the `requirements.txt` file that comes
with the SDK. To resolve these dependencies, you can use the PIP Dependency manager.
Install it by following steps at
[https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type
`pip --version`. This should display the version of the PIP Dependency Manager installed
if your installation was successful and the paths are properly defined.

- Using command line, navigate to the directory containing the generated files
  (including `requirements.txt`) for the SDK.
- Run the command `pip install -r requirements.txt`. This should install all the
  required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=Unifonic%20NextGen-Python)

## How to Use

The following section explains how to use the Unifonicnextgen SDK package in a new
project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable
if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=pyCharm)

Click on `Open` in PyCharm to browse to your generated SDK directory and then click
`OK`.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=openProject0&workspaceFolder=Unifonic%20NextGen-Python)

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=openProject1&workspaceFolder=Unifonic%20NextGen-Python&projectName=unifonicnextgen)

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=Unifonic%20NextGen-Python&projectName=unifonicnextgen)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)

Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=Unifonic%20NextGen-Python&projectName=unifonicnextgen)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using
the following code lines

```Python
from unifonicnextgen.unifonicnextgen_client import UnifonicnextgenClient
```

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=Unifonic%20NextGen-Python&libraryName=unifonicnextgen.unifonicnextgen_client&projectName=unifonicnextgen&className=UnifonicnextgenClient)

After this you can write code to instantiate an API client object, get a controller
object and make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your
Test project and click on `Run`

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=Unifonic%20NextGen-Python&libraryName=unifonicnextgen.unifonicnextgen_client&projectName=unifonicnextgen&className=UnifonicnextgenClient)

## How to Test

You can test the generated SDK and the server with automatically generated test cases.
unittest is used as the testing framework and nose is used as the test runner. You can
run the tests as follows:

1. From terminal/cmd navigate to the root directory of the SDK.
2. Invoke `pip install -r test-requirements.txt`
3. Invoke `nosetests`

## Initialization

### Authentication

In order to setup authentication and initialization of the API client, you need the
following information.

| Parameter            | Description                                   |
| -------------------- | --------------------------------------------- |
| basic_auth_user_name | The username to use with basic authentication |
| basic_auth_password  | The password to use with basic authentication |

API client can be initialized as following.

```python
# Configuration parameters and credentials
basic_auth_user_name = 'basic_auth_user_name' # The username to use with basic authentication
basic_auth_password = 'basic_auth_password' # The password to use with basic authentication

client = UnifonicnextgenClient(basic_auth_user_name, basic_auth_password)
```

# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

- [RestController](#rest_controller)
- [WrapperController](#wrapper_controller)

## <a name="rest_controller"></a>![Class: ](https://apidocs.io/img/class.png ".RestController") RestController

### Get controller instance

An instance of the `RestController` class can be accessed from the API Client.

```python
 rest_controller = client.rest
```

### <a name="delete_stop_scheduled_messages"></a>![Method: ](https://apidocs.io/img/method.png ".RestController.delete_stop_scheduled_messages") delete_stop_scheduled_messages

> Unifonic Stop scheduled messages API allows you to Delete (Stops) scheduled message,If
> MessageID is specified only one message is stopped, Otherwise all messages are stopped
> through simple RESTful APIs.

```python
def delete_stop_scheduled_messages(self,
                                       app_sid,
                                       message_id=None,
                                       response_format=None,
                                       base_encode=None)
```

#### Parameters

| Parameter      | Tags       | Description                                                                          |
| -------------- | ---------- | ------------------------------------------------------------------------------------ |
| appSid         | `Required` | A character string that uniquely identifies your app                                 |
| messageID      | `Optional` | A unique ID that identifies a message                                                |
| responseFormat | `Optional` | support json format only                                                             |
| baseEncode     | `Optional` | Binary-to-text encoding schemes that represent binary data in an ASCII string format |

#### Example Usage

```python
app_sid = '6v253153s1g7831s5'
message_id = 3200017889502
response_format = 'responseFormat'
base_encode = True

result = rest_controller.delete_stop_scheduled_messages(app_sid, message_id, response_format, base_encode)

```

#### Errors

| Error Code | Error Description                         |
| ---------- | ----------------------------------------- |
| 401        | Authentication failed                     |
| 455        | Scheduled message not found for this User |

### <a name="create_send_scheduled_messages"></a>![Method: ](https://apidocs.io/img/method.png ".RestController.create_send_scheduled_messages") create_send_scheduled_messages

> Unifonic Send Scheduled API allows you to schedule text messages to users around the
> globe through simple RESTful API to be sent in future.

```python
def create_send_scheduled_messages(self,
                                       app_sid,
                                       sender_id,
                                       recipient,
                                       body,
                                       time_scheduled,
                                       response_type=None,
                                       correlation_id=None,
                                       base_encode=None)
```

#### Parameters

| Parameter     | Tags       | Description                                                                                                     |
| ------------- | ---------- | --------------------------------------------------------------------------------------------------------------- |
| appSid        | `Required` | A character string that uniquely identifies your app                                                            |
| senderID      | `Required` | The SenderID to send from, App default SenderID is used unless else stated                                      |
| recipient     | `Required` | Destination mobile number, mobile numbers must be in international format without 00 or + Example: (4452023498) |
| body          | `Required` | Message body supports both English and unicodes characters, concatenated messages is supported                  |
| timeScheduled | `Required` | Schedule send messages, in the following format yyyy-mm-dd HH:mm:ss                                             |
| responseType  | `Optional` | Support json format only                                                                                        |
| correlationID | `Optional` | Is a unique identifier value that is attached to requests and messages                                          |
| baseEncode    | `Optional` | Binary-to-text encoding schemes that represent binary data in an ASCII string format                            |

#### Example Usage

```python
app_sid = '6v253153s1g7831s5'
sender_id = 'sender'
recipient = 966505980169
body = 'Test'
time_scheduled = 2020-04-12 11:50:00
response_type = 'responseType'
correlation_id = 'CorrelationID'
base_encode = True

result = rest_controller.create_send_scheduled_messages(app_sid, sender_id, recipient, body, time_scheduled, response_type, correlation_id, base_encode)

```

#### Errors

| Error Code | Error Description                                        |
| ---------- | -------------------------------------------------------- |
| 401        | Authentication failed                                    |
| 406        | Wrong parameter format                                   |
| 449        | Message body is empty                                    |
| 451        | TimeScheduled parameter must indicate time in the future |
| 480        | This user cannot use specified SenderID                  |
| 482        | Invalid dest num                                         |

### <a name="create_get_message_details"></a>![Method: ](https://apidocs.io/img/method.png ".RestController.create_get_message_details") create_get_message_details

> Unifonic Get message details API allows you to get details of messages with optional
> filters,returns paginated messages, next page or previous page through simple RESTful
> APIs

```python
def create_get_message_details(self,
                                   app_sid,
                                   message_id=None,
                                   sender_id=None,
                                   recipient=None,
                                   date_from=None,
                                   date_to=None,
                                   correlation_id=None,
                                   limit=None,
                                   base_encode=None)
```

#### Parameters

| Parameter     | Tags       | Description                                                                                                     |
| ------------- | ---------- | --------------------------------------------------------------------------------------------------------------- |
| appSid        | `Required` | A character string that uniquely identifies your app                                                            |
| messageID     | `Optional` | A unique ID that identifies a message                                                                           |
| senderID      | `Optional` | The SenderID to send from, App default SenderID is used unless else stated                                      |
| recipient     | `Optional` | Destination mobile number, mobile numbers must be in international format without 00 or + Example: (4452023498) |
| dateFrom      | `Optional` | The start date for the report time interval, date format should be yyyy-mm-dd                                   |
| dateTo        | `Optional` | The end date for the report time interval, date format should be yyyy-mm-dd                                     |
| correlationID | `Optional` | Is a unique identifier value that is attached to requests and messages                                          |
| limit         | `Optional` | The maximum number of messages details                                                                          |
| baseEncode    | `Optional` | Binary-to-text encoding schemes that represent binary data in an ASCII string format                            |

#### Example Usage

```python
app_sid = '6v253153s1g7831s5'
message_id = 2000000172800
sender_id = 'sender'
recipient = 966505980169
date_from = 2018-04-12
date_to = 2018-09-12
correlation_id = 'CorrelationID'
limit = 20
base_encode = True

result = rest_controller.create_get_message_details(app_sid, message_id, sender_id, recipient, date_from, date_to, correlation_id, limit, base_encode)

```

#### Errors

| Error Code | Error Description         |
| ---------- | ------------------------- |
| 401        | Authentication failed     |
| 432        | MessageId must be numeric |
| 599        | Request failed            |

### <a name="get_scheduled_message_details"></a>![Method: ](https://apidocs.io/img/method.png ".RestController.get_scheduled_message_details") get_scheduled_message_details

> Unifonic Scheduled message details allows you to get details of scheduled messages
> through simple RESTful APIs

```python
def get_scheduled_message_details(self,
                                      app_sid)
```

#### Parameters

| Parameter | Tags       | Description                                          |
| --------- | ---------- | ---------------------------------------------------- |
| appSid    | `Required` | A character string that uniquely identifies your app |

#### Example Usage

```python
app_sid = '6v253153s1g7831s5'

result = rest_controller.get_scheduled_message_details(app_sid)

```

#### Errors

| Error Code | Error Description     |
| ---------- | --------------------- |
| 401        | Authentication failed |

### <a name="create_send_message"></a>![Method: ](https://apidocs.io/img/method.png ".RestController.create_send_message") create_send_message

> Unifonic Send API allows you to send text messages to users around the globe through
> simple RESTful APIs

```python
def create_send_message(self,
                            app_sid,
                            sender_id,
                            body,
                            recipient,
                            response_type=None,
                            correlation_id=None,
                            base_encode=None,
                            status_callback=None,
                            async=False)
```

#### Parameters

| Parameter      | Tags                      | Description                                                                                                     |
| -------------- | ------------------------- | --------------------------------------------------------------------------------------------------------------- |
| appSid         | `Required`                | A character string that uniquely identifies your app                                                            |
| senderID       | `Required`                | The SenderID to send from, App default SenderID is used unless else stated                                      |
| body           | `Required`                | Message body supports both English and unicodes characters, concatenated messages is supported                  |
| recipient      | `Required`                | Destination mobile number, mobile numbers must be in international format without 00 or + Example: (4452023498) |
| responseType   | `Optional`                | Support json format only                                                                                        |
| correlationID  | `Optional`                | Is a unique identifier value that is attached to requests and messages                                          |
| baseEncode     | `Optional`                | Binary-to-text encoding schemes that represent binary data in an ASCII string format                            |
| statusCallback | `Optional`                | Filter messages report according to a specific message status, "Sent", "Queued", "Rejected" or "Failed          |
| async          | `Optional` `DefaultValue` | It specifies that the request will be executed asynchronously as soon as it is sent                             |

#### Example Usage

```python
app_sid = '6v253153s1g7831s5'
sender_id = 'sender'
body = 'Test'
recipient = 966505980169
response_type = 'responseType'
correlation_id = 'CorrelationID'
base_encode = True
status_callback = 'statusCallback'
async = False

result = rest_controller.create_send_message(app_sid, sender_id, body, recipient, response_type, correlation_id, base_encode, status_callback, async)

```

#### Errors

| Error Code | Error Description                       |
| ---------- | --------------------------------------- |
| 401        | Authentication failed                   |
| 449        | Message body is empty                   |
| 480        | This user cannot use specified SenderID |
| 482        | Invalid dest num                        |

[Back to List of Controllers](#list_of_controllers)

## <a name="wrapper_controller"></a>![Class: ](https://apidocs.io/img/class.png ".WrapperController") WrapperController

### Get controller instance

An instance of the `WrapperController` class can be accessed from the API Client.

```python
 wrapper_controller = client.wrapper
```

### <a name="create_get_msg_query"></a>![Method: ](https://apidocs.io/img/method.png ".WrapperController.create_get_msg_query") create_get_msg_query

> Unifonic Get message query API allows you to get details of specified message.

```python
def create_get_msg_query(self,
                             appsid,
                             msgid,
                             to=None)
```

#### Parameters

| Parameter | Tags       | Description                                                                                                     |
| --------- | ---------- | --------------------------------------------------------------------------------------------------------------- |
| appsid    | `Required` | A character string that uniquely identifies your app                                                            |
| msgid     | `Required` | A unique ID that identifies a message                                                                           |
| to        | `Optional` | Destination mobile number, mobile numbers must be in international format without 00 or + Example: (4452023498) |

#### Example Usage

```python
appsid = '6v253153s1g7831s5'
msgid = 3200017891630
to = 966505980169

result = wrapper_controller.create_get_msg_query(appsid, msgid, to)

```

#### Errors

| Error Code | Error Description                                         |
| ---------- | --------------------------------------------------------- |
| 401        | Authentication failed                                     |
| 402        | Missing parameter AppSid                                  |
| 432        | MessageId must be numeric                                 |
| 452        | User must specify either messageId or recipient parameter |

### <a name="create_send_message"></a>![Method: ](https://apidocs.io/img/method.png ".WrapperController.create_send_message") create_send_message

> Unifonic Send Wrapper API allows you to send text messages to multiple users at the
> same time

```python
def create_send_message(self,
                            appsid,
                            msg,
                            to,
                            sender,
                            base_encode=False,
                            encoding='UCS2')
```

#### Parameters

| Parameter  | Tags                      | Description                                                                                                        |
| ---------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| appsid     | `Required`                | A character string that uniquely identifies your app                                                               |
| msg        | `Required`                | Message body supports both English and unicodes characters, concatenated messages is supported                     |
| to         | `Required`                | Destination mobile number, mobile numbers must be in international format without 00 or + Example: (4452023498)    |
| sender     | `Required`                | The SenderID to send from, App default SenderID is used unless else stated                                         |
| baseEncode | `Optional` `DefaultValue` | Binary-to-text encoding schemes that represent binary data in an ASCII string format                               |
| encoding   | `Optional` `DefaultValue` | Converts information from a source into symbols for communication or storage, GSM7 for English and UCS2 for Arabic |

#### Example Usage

```python
appsid = '6v253153s1g7831s5'
msg = 'Test'
to = 966505980169
sender = 'sender'
base_encode = False
encoding = 'UCS2'

result = wrapper_controller.create_send_message(appsid, msg, to, sender, base_encode, encoding)

```

#### Errors

| Error Code | Error Description                                        |
| ---------- | -------------------------------------------------------- |
| 401        | Authentication failed                                    |
| 402        | Missing parameter AppSid                                 |
| 459        | Authentication parameters are incorrectly base64 encoded |

[Back to List of Controllers](#list_of_controllers)
