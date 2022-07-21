const cls = document.getElementById('v6Chat');

cls.textContent = '';

var statsus = document.createElement('label');
statsus.setAttribute('id', 'cheeckystatus');
statsus.innerHTML = 'We are IDLING';        
cls.appendChild(statsus)

var b7 = document.createElement("div");
b7.innerHTML = "&nbsp;";
cls.appendChild(b7)

var input99 = document.createElement("div");   
input99.setAttribute("type", "text");
input99.setAttribute("size", "1")
input99.setAttribute("id", "commandline")
input99.setAttribute('contenteditable', 'true')
input99.style.color = 'black'
input99.style.padding = '2'
input99.style.backgroundColor = "#FF0000";     
input99.innerHTML = "I am a command line";
cls.appendChild(input99)

var b99 = document.createElement("div");       
b99.innerHTML = "&nbsp;";
cls.appendChild(b99)

var input0 = document.createElement("div");   
input0.setAttribute("type", "text");
input0.setAttribute("size", "1")
input0.setAttribute("id", "string0")
input0.setAttribute('contenteditable', 'true')
input0.style.color = 'black'
input0.style.padding = '2'
input0.style.backgroundColor = "#00FF00";     
input0.innerHTML = "- - - - - - -";
cls.appendChild(input0)

var b0 = document.createElement("div");       
b0.innerHTML = "&nbsp;";
cls.appendChild(b0)



var input1 = document.createElement("div");   
input1.setAttribute("type", "text");
input1.setAttribute("size", "1")
input1.setAttribute("id", "string1")
input1.setAttribute('contenteditable', 'true')
input1.style.color = 'black'
input1.style.padding = '2'
input1.style.backgroundColor = "#00FF00";     
input1.innerHTML = "- - - - - - -";
cls.appendChild(input1)

var b1 = document.createElement("div");       
b1.innerHTML = "&nbsp;";
cls.appendChild(b1)



var input2 = document.createElement("div");   
input2.setAttribute("type", "text");
input2.setAttribute("size", "1")
input2.setAttribute("id", "string2")
input2.setAttribute('contenteditable', 'true')
input2.style.color = 'black'
input2.style.padding = '2'
input2.style.backgroundColor = "#00FF00";     
input2.innerHTML = "- - - - - - -";
cls.appendChild(input2)

var b2 = document.createElement("div");
b2.innerHTML = "&nbsp;";
cls.appendChild(b2)



var input3 = document.createElement("div");
input3.setAttribute("type", "text");
input3.setAttribute("size", "1")
input3.setAttribute("id", "string3")
input3.setAttribute('contenteditable', 'true')
input3.style.color = 'black'
input3.style.padding = '2'
input3.style.backgroundColor = "#00FF00";
input3.innerHTML = "- - - - - - -";
cls.appendChild(input3)

var b3 = document.createElement("div");
b3.innerHTML = "&nbsp;";
cls.appendChild(b3)



var input4 = document.createElement("div");
input4.setAttribute("type", "text");
input4.setAttribute("size", "1")
input4.setAttribute("id", "string4")
input4.setAttribute('contenteditable', 'true')
input4.style.color = 'black'
input4.style.padding = '2'
input4.style.backgroundColor = "#00FF00";
input4.innerHTML = "- - - - - - -";
cls.appendChild(input4)

var b4 = document.createElement("div");
b4.innerHTML = "&nbsp;";
cls.appendChild(b4)



var input5 = document.createElement("div");
input5.setAttribute("type", "text");
input5.setAttribute("size", "1")
input5.setAttribute("id", "string5")
input5.setAttribute('contenteditable', 'true')
input5.style.color = 'black'
input5.style.padding = '2'
input5.style.backgroundColor = "#00FF00";
input5.innerHTML = "- - - - - - -";
cls.appendChild(input5)

var b5 = document.createElement("div");
b5.innerHTML = "&nbsp;";
cls.appendChild(b5)



var input6 = document.createElement("div");
input6.setAttribute("type", "text");
input6.setAttribute("size", "1")
input6.setAttribute("id", "string6")
input6.setAttribute('contenteditable', 'true')
input6.style.color = 'black'
input6.style.padding = '2'
input6.style.backgroundColor = "#00FF00";
input6.innerHTML = "- - - - - - -";
cls.appendChild(input6)

var b6 = document.createElement("div");
b6.innerHTML = "&nbsp;";
cls.appendChild(b6)



var output = document.createElement('label');
output.setAttribute('id', 'cheeckyoutput');
output.innerHTML = 'I will contain answers in a while :-)';        
cls.appendChild(output)