# Hotelsoft Python coding test

# Environment setup

The laptop has necessary python modules installed.  To use proper python environment use the following steps:

> Launch iTerm
> 
> At the prompt type `workon pyenv`

This will setup all the required python environment


## Exercise: Processing reservations file for analytical purposes

Write a program which will take a reservation file as an argument (use the sample reservations.csv file)

Structure of the reservation CSV file is like below:

| Extract Date | ResortID | Reservation ID | Confirmation No | BookTime             | Status | Arrival              | Departure            | Stay Date            | Adults | Children | Nights | RateCode | RateCodeName    | RateCategory | RoomType | Quantity | Packages | Room Revenue | Package Revenue | Other Revenue | Reservation Type | MarketCode | Market Name | Source Description   | Origin | Company ID | Company Name | Travel Agent ID | Block ID | Guest ID | FirstName | LastName | Update Date          | RoutingCode | Modify Date          | GstAddress         | GstCity   | GstRegion | GstRegionCode | GstZip | GstCountryCode | 
|--------------|----------|----------------|-----------------|----------------------|--------|----------------------|----------------------|----------------------|--------|----------|--------|----------|-----------------|--------------|----------|----------|----------|--------------|-----------------|---------------|------------------|------------|-------------|----------------------|--------|------------|--------------|-----------------|----------|----------|-----------|----------|----------------------|-------------|----------------------|--------------------|-----------|-----------|---------------|--------|----------------| 
| 2018-07-20   | 14894    | 52555591       | 0ASLKQR46       | 7/14/2018 5:32:00 PM | N      | 8/4/2018 12:00:00 AM | 8/7/2018 12:00:00 AM | 8/4/2018 12:00:00 AM | 1      | 0        | 3      | B-AAA    | AAA Member Rate | Association  | KING     | 1        |          | 287.100000   | 0.000000        | 0.0           | Transient        |            |             | Booking Engine (IBE) |        | 0          |              | 0               | 0        | 0        | Leanne    | Johnson  | 7/14/2018 5:32:00 PM |             | 7/14/2018 5:32:00 PM | 209 Danville Drive | Los Gatos |           | CA            | 95032  | US             | 
| 2018-07-20   | 14894    | 52555591       | 0ASLKQR46       | 7/14/2018 5:32:00 PM | N      | 8/4/2018 12:00:00 AM | 8/7/2018 12:00:00 AM | 8/5/2018 12:00:00 AM | 1      | 0        | 3      | B-AAA    | AAA Member Rate | Association  | KING     | 1        |          | 188.100000   | 0.000000        | 0.0           | Transient        |            |             | Booking Engine (IBE) |        | 0          |              | 0               | 0        | 0        | Leanne    | Johnson  | 7/14/2018 5:32:00 PM |             | 7/14/2018 5:32:00 PM | 209 Danville Drive | Los Gatos |           | CA            | 95032  | US             | 
| 2018-07-20   | 14894    | 52555591       | 0ASLKQR46       | 7/14/2018 5:32:00 PM | N      | 8/4/2018 12:00:00 AM | 8/7/2018 12:00:00 AM | 8/6/2018 12:00:00 AM | 1      | 0        | 3      | B-AAA    | AAA Member Rate | Association  | KING     | 1        |          | 188.100000   | 0.000000        | 0.0           | Transient        |            |             | Booking Engine (IBE) |        | 0          |              | 0               | 0        | 0        | Leanne    | Johnson  | 7/14/2018 5:32:00 PM |             | 7/14/2018 5:32:00 PM | 209 Danville Drive | Los Gatos |           | CA            | 95032  | US             | 

Key Columns for analysis are: 

* Reservation ID - Reservation Id
* BookTime - When the reservation is booked
* Status - Status of reservation
* Arrival - Guest arrival date
* Departure - Guest departure date
* RateCategory - Rate category code
* Room Revenue - Room rate for a given stay night
* Block ID - Non zero indicates reservations are part of block.
* Guest ID - Guest ID
* GstCity - Guest City code
* GstZip - Guest ZIP code
* GstCountryCode - Guest country code

Each reservation is repeated for staynight as a separate row.  Example if a reservation is for 2 nights the file will contain 2 repeated rows one for each staynight.

---
> For all the questions below ignore cancelled reservations (Status == 'C')

> All the repeated reservations need to be combined into one single reservation with Room Revenue added up

> All top reservations are sorted based on revenue unless specified differently 
---

### Question

Find top 10 paying customers excluding block reservations.  Output should display as follows:

| Guest ID | FirstName | LastName | Revenue | 
|----------|-----------|----------|---------| 
| 1234     | Test      | User1    | 2039.39 | 
| 1235     | Test      | User2    | 2020.25 | 


### Question

Find top 10 block reservations (Block ID > 0) based on number of staynights.  Output should display as follows:

| Block ID | Stay nights | 
|----------|-------------| 
| 1234     | 200         | 
| 1235     | 100         | 

### Question

Find top 10 reservations which have long booking window.

> Bookingwindow = Number of days (Arrival - BookTime)




### Question

Find top 10 countries within each country top 5 cities within each city top 5 zipcodes.  Output should display the following:

| Country | City          | Zipcode | Revenue | 
|---------|---------------|---------|---------| 
| US      | San Francisco | 94104   | 180000  | 
| US      | San Francisco | 94114   | 170000  | 
| US      | San Francisco | 94119   | 165000  | 
| US      | San Francisco | 94125   | 163000  | 
| US      | San Francisco | 94153   | 160000  | 
| US      | Houston       | 77007   | 15500   | 
| US      | Houston       | 77044   | 15400   | 
| US      | Houston       | 77010   | 15300   | 
| US      | Houston       | 77050   | 15200   | 
| US      | Houston       | 77061   | 15100   | 


### Question


