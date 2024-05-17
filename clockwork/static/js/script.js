var items = document.querySelectorAll('#container > div');
    var itemsPerPage = 10;
    var currentPage = 0;

    function showPage(page) {
        var startIndex = page * itemsPerPage;
        var endIndex = (page + 1) * itemsPerPage;

        for (var i = 0; i < items.length; i++) {
            if (i >= startIndex && i < endIndex) {
                items[i].style.display = 'block';
            } else {
                items[i].style.display = 'none';
            }
        }
    }

    function nextPage() {
        currentPage++;
        showPage(currentPage);
    }

    function previousPage() {
        currentPage--;
        if (currentPage < 0) {
            currentPage = 0;
        }
        showPage(currentPage);
    }

    // Показываем первую страницу при загрузке
    showPage(currentPage);