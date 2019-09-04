# abap python googlespreadsheet
 SAP ABAP get data from Google Spreadsheet using Python
 
 
1. Create GoogleSpreadsheet
2. Create GoogleAppScript code (see file googleappscript)
Tools -> Script editor   
copy & paste URL GoogleSpreadsheet to the code
3. Publish -> Deploy as web app
Who has access to the app: - Anyone, even anonymus
4. Create Python code (see app.py)
5. Copy & paste the URL GoogleAppScript to Python code
6. Test @ Postman : GET Params : http://127.0.0.1:5000
the output:
[{"InvoiceID":"123-19-1176","ProductLine":"HEALTH AND BEAUTY","UnitPrice":58.22,"Quantity":3,"DatePurchase":20190901}, . .{ }]
