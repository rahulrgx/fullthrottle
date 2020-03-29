# fullthrottle
Rest API for user and activity period
Steps taken in the making of this API.
Step:1
first of all i created model i.e user and activityperiod model also put all the relation(one to many) between user and activityperiod model.
Step 2:
Added url configuration for REST API.
Step 3:
I created view for user and activityperiod.
Step 4:
From the third step i added ORM querry to fetch the data from the database  (sqlite) using view set concept.
Step: 5
Serialize all user and activityperiod model as JASON response, so client can fetch the data as JASON response.
Note: from the backend we are getting the JASON response therefore the frontend developer will be able to display the data in the desired format like table and list format. 


