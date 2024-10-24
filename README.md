# Project Networking


> **Don't forget to edit this `README.md` file**
>
> If you're interested in how to format markdown, click [here](https://www.markdownguide.org/basic-syntax/#images-1)

## API Overview
My API includes a database with a diverse selection of exercises and stretches that can help climbers improve their climbing ability. 

**Some of the features in this API include:**  

-viewing all the exercises and stretches

-filtering to only see one exercise or stretch at a time 

-filtering to see all of one category (e.g. seeing all of the exercises but no stretches)

-likeing certain exercises or stretches that you like to show your support and reccomend it to others

-change and edit the information of existing exercises and stretches if you find any mistakes or any areas of improvement

-searching for certain exercises or stretches based on keywords they contain



### Model
*Model Name:* Exercise

| Field Names  | Field Data Types |
|--------------|------------------|
| name         | StringField()    |
| category     | StringField()    |
| instructions | StringField()    |
| extra        | IntegerField()   |
| likes        | IntegerField()   |
| views        | IntegerField()   |

| Method Name        | Included Field Names and Data Type                                                                                                    | Parameter                                 | Description                                                                                     |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|-------------------------------------------------------------------------------------------------|
| Json_response      | id name:StringField() category:StringField() instructions:StringField() extra:StringField() likes:IntegerField() views:IntegerField() |          self                                      | Returns the properties                                                                          |
| increase_likes     | likes:IntegerField()                                                                                                                  | self                                      | Increases the likes for a certain exercise or stretch                                           |
| increase_views     | views:IntegerField()                                                                                                                  | self                                      | Increases the views for an exercise or stretch that you have viewed when using the route 'one'  |
| change_information | name:StringField() category:StringField() instructions:StringField() extra:StringField() likes:IntegerField()                         | self, name, category, instructions, extra | Changes the information for a certain exercise or stretch                                       |

### Endpoints

| Route Name | HTTP Method | Payload                                                             | Description                                                                                                                                                   |
|------------|-------------|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /all       | get         | none required                                                       | Returns all of both exercises and stretches that are in the database                                                                                          |
| /one       | get         | id : int                                                            | Returns one certain exercise or stretch that the user entered the id of                                                                                       |
| /new       | post        | name:str        category:str         instructions:str     extra:str | Users can create a completely new exercise or stretch by entering all of the required payloads                                                                |
| /category  | get         | category:str                                                        | Filters to a certain category (exercise/stretch)                                                                                                              |
| /edit      | post        | name:str category:str instructions:str      extra : str                     | Users can edit information on existing exercises and stretches by entering the id of the one they want to change and entering all of the required information |
| /likes     | post        | id:int                                                              | Users can like a certain exercise or stretch by entering its id                                                                                               |
| /search    | get         | keyword:str                                                         | Users can enter specific keywords to find certain exercises or stretches that includes the keyword                                                            |


---

## Setup

### Contents

Here's what is included:
- `\app`
    - `models.py` - `Fortune` model
    - `views.py` - endpoints
- `database.sqlite`  
- `README.md` 

**To start a Banjo server:** `banjo` 
- [Banjo Documentation](https://the-isf-academy.github.io/banjo_docs/)



