var selected = function(ele) {
    ele.style.pointerEvents = 'none';
    ele.style.background = '#add0fe';
    ele.style.color = '#2f89fc';
    ele.style.border = '1px solid transparent';
}

var disabled = function(ele) {
    ele.style.pointerEvents = 'none';
    ele.style.background = '#e0e0e0';
    ele.style.borderRadius = '50%';
    ele.style.color = '#a0a0a0';
    ele.style.border = '1px solid transparent';
}

var enabled = function(ele) {
    ele.style.pointerEvents = 'auto';
    ele.style.background = 'transparent';
    ele.style.borderRadius = '50%';
    ele.style.border = '1px solid #add0fe';
    ele.style.color = '#2f89fc';
}

var initLayout = function() {
    var projects = document.getElementsByClassName('project-card');
    for (var i = 10; i < projects.length; i++) projects[i].style.display = 'none';
    
    var prevButton = document.getElementById('prev-button');
    disabled(prevButton);

    var pageButtons = document.getElementsByClassName('page-button');
    selected(pageButtons[0]);

    var nextButton = document.getElementById('next-button');
    if (projects.length == 1) disabled(nextButton);

    for (var i = 0; i < pageButtons.length; i++) {
        pageButtons[i].addEventListener('click', function() {
            var projects = document.getElementsByClassName('project-card');
            var page = parseInt(this.getAttribute('data-page'));
            var pageButtons = document.getElementsByClassName('page-button');
            var prevButton = document.getElementById('prev-button');
            var nextButton = document.getElementById('next-button');

            for (var j = 0; j < pageButtons.length; j++)
                enabled(pageButtons[j]);
            selected(this);

            if (page != 1) enabled(prevButton);
            else disabled(prevButton);

            if (page != pageButtons.length) enabled(nextButton);
            else disabled(nextButton);

            for (var i = 0; i < projects.length; i++) projects[i].style.display = 'none';
            for (var i = (page - 1) * 10; i < Math.min(projects.length, page * 10); i++) projects[i].style.display = 'block';

            document.getElementById('projects-layout').setAttribute('data-current-page', page);

            return false;
        });
    }

    prevButton.addEventListener('click', function() {
        var currentPage = parseInt(document.getElementById('projects-layout').getAttribute('data-current-page'));
        var projects = document.getElementsByClassName('project-card');
        var pageButtons = document.getElementsByClassName('page-button');
        var nextButton = document.getElementById('next-button');

        for (var j = 0; j < pageButtons.length; j++)
            enabled(pageButtons[j]);
        selected(pageButtons[currentPage - 2]);

        if (currentPage != 2) enabled(this);
        else disabled(this);

        enabled(nextButton);

        for (var i = 0; i < projects.length; i++) projects[i].style.display = 'none';
        for (var i = (currentPage - 2) * 10; i < (currentPage - 1) * 10; i++) projects[i].style.display = 'block';

        document.getElementById('projects-layout').setAttribute('data-current-page', currentPage - 1);

        return false;
    });

    nextButton.addEventListener('click', function() {
        var currentPage = parseInt(document.getElementById('projects-layout').getAttribute('data-current-page'));
        var projects = document.getElementsByClassName('project-card');
        var pageButtons = document.getElementsByClassName('page-button');
        var prevButton = document.getElementById('prev-button');

        for (var j = 0; j < pageButtons.length; j++)
            enabled(pageButtons[j]);
        selected(pageButtons[currentPage]);

        if (currentPage != pageButtons.length - 1) enabled(this);
        else disabled(this);

        enabled(prevButton);

        for (var i = 0; i < projects.length; i++) projects[i].style.display = 'none';
        for (var i = currentPage * 10; i < Math.min(projects.length, (currentPage + 1) * 10); i++) projects[i].style.display = 'block';

        document.getElementById('projects-layout').setAttribute('data-current-page', currentPage + 1);

        return false;
    });
}
initLayout();

var search = function() {
    var input = document.getElementById('search-input');

    var whatIsDisplayed = document.getElementById('whatIsDisplayed');
    var whatIsDisplayedOriginal = whatIsDisplayed.innerHTML;

    var searchStatus = document.getElementById('search-status');
    searchStatus.style.display = 'none';

    var noResults = document.getElementById('no-results');
    noResults.style.display = 'none';

    fetch('../../data/projects.json')
    .then(response => response.json())
    .then(projectsData => {
        // Search function regex match
        input.addEventListener('keyup', function() {
            var searchString = input.value.toLowerCase();
            var paginationControls = document.getElementById('pagination-controls');
            var projects = document.getElementsByClassName('project-card');
            var projectsLayout = document.getElementById('projects-layout');
            var regex = new RegExp(searchString, 'g');

            if (searchString.length > 0) {
                paginationControls.style.display = 'none';
                searchStatus.style.display = 'block';
                var matchedProjects = [];
                var foundMatches = false;

                for(var i = 0; i < projects.length; i++) {
                    var project = projects[i];
                    var projectUrl = project.getAttribute('data-project-key');
                    var projectData = projectsData[projectUrl];

                    var description = projectData.description.toLowerCase();
                    var title = projectData.title.toLowerCase();
                    var projectUrlMatch = projectUrl == searchString;
                    var titleMatch = title.match(regex);
                    var descriptionMatch = description.match(regex);
                    var urlSplit = projectUrl.split('-');
                    var urlMatch = false;
                    for (var j = 0; j < urlSplit.length; j++) {
                        var urlPart = urlSplit[j].toLowerCase();
                        if (urlPart.match(regex)) {
                            urlMatch = true;
                        }
                    }

                    whatIsDisplayed.innerHTML = searchString.length > 0 ? 'Displaying results for: ' + searchString : whatIsDisplayedOriginal;

                    if(titleMatch || descriptionMatch || projectUrlMatch || urlMatch) {
                        matchedProjects.push(i);
                        foundMatches = true;
                    } 

                    project.style.display = 'none';
                }

                searchStatus.innerHTML = foundMatches ? '(Found ' + matchedProjects.length + ' projects)' : '';
                noResults.style.display = !foundMatches ? 'block' : 'none';

                for(var i = 0; i < projects.length; i++) if (matchedProjects.indexOf(i) > -1) projects[i].style.display = 'block';
            }
            else {
                paginationControls.style.display = 'flex';
                whatIsDisplayed.innerHTML = whatIsDisplayedOriginal;
                searchStatus.innerHTML = '';
                searchStatus.style.display = 'none';
                noResults.style.display = 'none';

                var currentPage = parseInt(projectsLayout.getAttribute('data-current-page'));
                for (var i = 0; i < projects.length; i++) projects[i].style.display = 'none';
                for (var i = (currentPage - 1) * 10; i < Math.min(projects.length, currentPage * 10); i++) projects[i].style.display = 'block';
            }
        })
    })
}
search();