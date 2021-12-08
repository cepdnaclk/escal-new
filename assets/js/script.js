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