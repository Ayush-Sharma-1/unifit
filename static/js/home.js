    $(document).ready(function () {
        $("#country-dropdown,#department-dropdown").on("change", function () {
            var country = $('#country-dropdown').find("option:selected").val();
            var dept = $('#department-dropdown').find("option:selected").val();
            console.log("This is ready")
            SearchData(country, dept)
        });
    });
    function SearchData(country, dept) {
        if (country.toUpperCase() == 'ALL' && dept.toUpperCase() == 'ALL') {
            $('#unitable tbody tr').show();
        } else {
            $('#unitable tbody tr:has(td)').each(function () {
                var rowCountry = $.trim($(this).find('td:eq(1)').text());
                var rowDept = $.trim($(this).find('td:eq(2)').text());
                if (country.toUpperCase() != 'ALL' && dept.toUpperCase() != 'ALL') {
                    if (rowCountry.toUpperCase() == country.toUpperCase() && rowDept == dept) {
                        $(this).show();
                    } else {
                        $(this).hide();
                    }
                } else if ($(this).find('td:eq(1)').text() != '' || $(this).find('td:eq(1)').text() != '') {
                    if (country != 'all') {
                        if (rowCountry.toUpperCase() == country.toUpperCase()) {
                            $(this).show();
                        } else {
                            $(this).hide();
                        }
                    }
                    if (dept != 'all') {
                        if (rowDept == dept) {
                            $(this).show();
                        }
                        else {
                            $(this).hide();
                        }
                    }
                }
 
            });
        }
    }
