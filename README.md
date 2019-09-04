# abap python googlespreadsheet
 SAP ABAP get data from Google Spreadsheet using Python

![alt text](https://github.com/jenizar/abap-python-googlespreadsheet/blob/master/Screenshot.PNG)
 
1. Create GoogleSpreadsheet
2. Create GoogleAppScript code (see file googleappscript)
Tools -> Script editor   
copy & paste URL GoogleSpreadsheet to the code

![alt text](https://github.com/jenizar/abap-python-googlespreadsheet/blob/master/googleappscript.PNG)

3. Publish -> Deploy as web app
Who has access to the app: - Anyone, even anonymus
4. Create Python code (see app.py)
5. Copy & paste the URL GoogleAppScript to Python code
6. Test @ Postman : GET Params : http://127.0.0.1:5000

the output:
[{"InvoiceID":"123-19-1176","ProductLine":"HEALTH AND BEAUTY","UnitPrice":58.22,"Quantity":3,"DatePurchase":20190901}, . .{ }]

References:
1. https://github.com/jenizar/Google-Spreadsheet-Export-Data-to-MySQL-Database
2. https://stackoverflow.com/questions/31728937/render-json-without-replacing-characters-in-jinja/31729295#31729295
