(function($) {
        $.fn.loadChildChoices = function(child) {
            var valuefield = child;
            var ajax_url = valuefield.attr('ajax_url');
            var empty_label = valuefield.attr('empty_label') || '--------';

            $.get(
                ajax_url,
                {
                    field: valuefield.attr('name'),
                    parent_field: $(this).attr('name'),
                    parent_value: $(this).val()
                },
                function(j) {
                    var options = '';
                    var selected_value = child.val();
                    if (!child[0].hasAttribute('multiple'))
                        options += '<option value="">' + empty_label + '</option>';
                    for (var i = 0; i < j.length; i++) {
                        options += '<option value="' + j[i][0] + '">' + j[i][1] + '</option>';
                    }
                    valuefield.html(options);
                    valuefield.val(selected_value);  // keep selection on choices refresh
                    // TODO: Add an option whether to reload childs or not
                    // valuefield.trigger('change');
                    valuefield.trigger("liszt:updated"); // support for chosen versions < 1.0.0
                    valuefield.trigger("chosen:updated"); // support for chosen versions >= 1.0.0
                },
                "json"
            );
        };

        $.fn.loadAllChainedChoices = function() {
            var chained_ids = $(this).attr('chained_ids').split(",");

            for (var i = 0; i < chained_ids.length; i++) {
                var chained_id = chained_ids[i];

                $(this).loadChildChoices($('#' + chained_id));
            }
        };
})(jQuery || django.jQuery);
