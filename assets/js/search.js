var search = function() {
    var projects = document.getElementsByClassName('project-card');
    
    var input = document.getElementById('search-input');

    var whatIsDisplayed = document.getElementById('whatIsDisplayed');
    var whatIsDisplayedOriginal = whatIsDisplayed.innerHTML;

    var nothingToDisplay = document.getElementById('nothingToDisplay');
    nothingToDisplay.style.display = 'none';
    
    // Search function regex match
    input.addEventListener('keyup', function() {
        var searchString = input.value.toLowerCase();
        var regex = new RegExp(searchString, 'g');
        var founded = false;
        for(var i = 0; i < projects.length; i++) {
            var project = projects[i];
            var title = project.getElementsByClassName('heading').item(0).innerHTML.toLowerCase();
            var description = project.getElementsByClassName('project-description').item(0).innerHTML.toLowerCase();
            var projectUrl = project.dataset.projectUrl;
            var projectUrlMatch = projectUrl == searchString;
            var titleMatch = title.match(regex);
            var descriptionMatch = description.match(regex);
            var urlSplit = projectUrl.split('/');
            var urlMatch = false;
            for (var j = 0; j < urlSplit.length; j++) {
                var urlPart = urlSplit[j].toLowerCase();
                if (urlPart.match(regex)) {
                    urlMatch = true;
                }
            }

            whatIsDisplayed.innerHTML = searchString.length > 0 ? 'Displaying results for: ' + searchString : whatIsDisplayedOriginal;

            if(titleMatch || descriptionMatch || projectUrlMatch || urlMatch) {
                project.style.display = 'block';
                founded = true;
            } else {
                project.style.display = 'none';
            }
            founded ? nothingToDisplay.style.display = 'none' : nothingToDisplay.style.display = 'block';
        }
    })

   
}
search();