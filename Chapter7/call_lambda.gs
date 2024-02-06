function submitForm(e) { 

var responses = e.values;  

var size = responses[0]; 

var apiUrl = '<YOUR_LAMBDA_URL>'; 

var requestData = { 

'instance_size': size, 

}; 

 
 

var requestBody = JSON.stringify(requestData); 

var options = { 

'method': 'get', 

'contentType': 'application/json', 

'payload': requestBody, 

}; 

var response = UrlFetchApp.fetch(apiUrl, options); 

} 
