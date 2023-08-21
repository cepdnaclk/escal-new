var selected = function(ele) {
    ele.style.pointerEvents = 'none';
    ele.style.background = '#add0fe';
    ele.style.color = '#2f89fc';
    ele.style.border = '1px solid transparent';
    if (ele.classList.contains('disabled')) ele.classList.remove('disabled');
}

var disabled = function(ele) {
    ele.style.pointerEvents = 'none';
    ele.style.background = '#e0e0e0';
    ele.style.borderRadius = '50%';
    ele.style.color = '#a0a0a0';
    ele.style.border = '1px solid transparent';
    ele.parentElement.style.cursor = 'not-allowed';
    ele.classList.add('disabled');
}

var enabled = function(ele) {
    ele.style.pointerEvents = 'auto';
    ele.style.background = 'transparent';
    ele.style.borderRadius = '50%';
    ele.style.border = '1px solid #add0fe';
    ele.style.color = '#2f89fc';
    if (ele.classList.contains('disabled')) ele.classList.remove('disabled');
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
    var heading = document.getElementById('heading');

    var whatIsDisplayed = document.getElementById('whatIsDisplayed');
    var whatIsDisplayedOriginal = whatIsDisplayed.innerHTML;

    var searchStatus = document.getElementById('search-status');
    searchStatus.style.display = 'none';

    var noResults = document.getElementById('no-results');
    noResults.style.display = 'none';

    var projects = document.getElementsByClassName('project-card');
    var projIds = {}, projIdReverse = {};
    for (var i = 0; i < projects.length; i++) projIds[projects[i].getAttribute('data-id')] = i;

    var index = FlexSearch.Index({
        tokenize: 'forward',
        cache: true,
        context: true,
        language: 'en',
    });

    for (var i = 0; i < projects.length; i++) {
        var combinedDoc = projects[i].getAttribute('data-title') + ' ' + projects[i].getAttribute('data-description') + ' ' + projects[i].getAttribute('data-id').replace('-', ' ') + ' ' + projects[i].getAttribute('data-category');
        index.add(i, combinedDoc);
    }

    // Search function regex match
    input.addEventListener('keyup', function() {
        var searchString = input.value.toLowerCase();

        var paginationControls = document.getElementById('pagination-controls');
        var projectsLayout = document.getElementById('projects-layout');
        var regex = new RegExp(searchString, 'g');
        var foundMatches = false;
        var matchedProjects = [];

        if (searchString.length > 0) {
            for (var i = 0; i < projects.length; i++) projects[i].style.display = 'none';

            if (searchString.split(' ').length == 1) {
                paginationControls.style.display = 'none';
                searchStatus.style.display = 'block';

                for(var i = 0; i < projects.length; i++) {
                    var project = projects[i];
                    var repoUrl = project.getAttribute('data-id');
                    var description = project.getAttribute('data-description').toLowerCase();
                    var title = project.getAttribute('data-title').toLowerCase();
                    var category = project.getAttribute('data-category').toLowerCase();
                    var repoUrlMatch = repoUrl == searchString;
                    var titleMatch = title.match(regex);
                    var descriptionMatch = description.match(regex);
                    var categoryMatch = category.match(regex);
                    var urlSplit = repoUrl.split('-');
                    var urlMatch = false;
                    for (var j = 0; j < urlSplit.length; j++) {
                        var urlPart = urlSplit[j].toLowerCase();
                        if (urlPart.match(regex)) {
                            urlMatch = true;
                        }
                    }

                    if(titleMatch || descriptionMatch || repoUrlMatch || urlMatch || categoryMatch) {
                        matchedProjects.push(i);
                        foundMatches = true;
                    }
                }

                if (!foundMatches) {
                    matchedProjects = index.search(searchString);
                    foundMatches = matchedProjects.length > 0;
                }
            }
            else {
                matchedProjects = index.search(searchString);
                foundMatches = matchedProjects.length > 0;
            }

            if (foundMatches) {
                whatIsDisplayed.innerHTML = searchString.length > 0 ? 'Displaying top results for: ' + searchString : whatIsDisplayedOriginal;
                searchStatus.innerHTML = '(Found ' + matchedProjects.length + ' results)';
                noResults.style.display = 'none';
                heading.style.display = 'flex';
            }
            else {
                searchStatus.innerHTML = '';
                noResults.style.display = 'block';
                heading.style.display = 'none';
            }

            for(var i = 0; i < matchedProjects.length; i++) projects[matchedProjects[i]].style.display = 'block';
        }
        else {
            paginationControls.style.display = 'flex';
            heading.style.display = 'flex';
            whatIsDisplayed.innerHTML = whatIsDisplayedOriginal;
            searchStatus.innerHTML = '';
            searchStatus.style.display = 'none';
            noResults.style.display = 'none';

            var currentPage = parseInt(projectsLayout.getAttribute('data-current-page'));
            for (var i = 0; i < projects.length; i++) projects[i].style.display = 'none';
            for (var i = (currentPage - 1) * 10; i < Math.min(projects.length, currentPage * 10); i++) projects[i].style.display = 'block';
        }
    });
}
search();

var filterByTags = function() {
    document.addEventListener('DOMContentLoaded', function () {
        var tagCloudLinks = document.querySelectorAll('.tag-cloud-link');
        var projectCards = document.querySelectorAll('.project-card');
        var pageButtons = document.querySelectorAll('.page-button');
        var paginationControls = document.getElementById('pagination-controls');

        tagCloudLinks.forEach(function (tagCloudLink) {
            tagCloudLink.addEventListener('click', function (e) {
                e.preventDefault();
                var selectedCategoryCode = tagCloudLink.getAttribute('data-category-code');

                projectCards.forEach(function (projectCard) {
                    // filter by category, category.title, title
                    var projectCategory = projectCard.getAttribute('data-category').toLowerCase();
                    var projectCategorycode = projectCard.getAttribute('data-category-code').toLowerCase();
                    var projectTitle = projectCard.getAttribute('data-title').toLowerCase();
                    var shouldDisplay = selectedCategoryCode === 'all';

                    if (shouldDisplay || projectCategory.includes(selectedCategoryCode) || projectCategorycode.includes(selectedCategoryCode) || projectTitle.includes(selectedCategoryCode)) {
                        shouldDisplay = true;
                    }

                    projectCard.style.display = shouldDisplay ? 'block' : 'none';
                });

                paginationControls.style.display = (selectedCategoryCode === 'all') ? 'block' : 'none';

                // Trigger a click on the first page button
                if (selectedCategoryCode === 'all') {
                    pageButtons[0].click();
                }
            });
        });
    });
}
filterByTags();
