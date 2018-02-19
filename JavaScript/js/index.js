//loading dynamic table//
var tbody = document.querySelector("tbody");

var tableData = dataSet;

rendertable();

function rendertable(){
    tbody.innerHTML = "";
    for(var i=0;i<tableData.length;i++)
    {
        var address = tableData[i];
        var fields = Object.keys(address);
        var row=tbody.insertRow(i);
        for (var j=0;j<fields.length;j++)
        {
            var field=fields[j];
            var cell=row.insertCell(j);
            cell.innerText=address[field];
        }
    }

}

//search feature//
var dateInput = document.querySelector("#date");
var stateInput = document.querySelector("#state");
var cityInput = document.querySelector("#city");
var countryInput = document.querySelector("#country");
var shapeInput = document.querySelector("#shape");
var durationInput = document.querySelector("#duration");

var searchBtn = document.querySelector("#search");

searchBtn.addEventListener("click", handleSearchButtonClick);

function handleSearchButtonClick() 
{
    // if(dateInput.value!="")
    // {
        var filterDate = dateInput.value.trim();
        tableData = dataSet.filter(function(address)
         {
        var addressDate = address.datetime;
        return addressDate === filterDate;
    });
    rendertable();

    // }
    // else if(stateInput.value!="")
    // {
    //     var filterState = stateInput.value.trim().toLowerCase();
    //     tableData = dataSet.filter(function(address) {
    //       var addressState = address.state.toLowerCase();
      
    //       // If true, add the address to the filteredAddresses, otherwise don't add it to filteredAddresses
    //       return addressState === filterState;
    //     });
    //     rendertable();
    // }
    // else {
    //     console.log("No filter condition");
    // }
}