// lazyload config

angular.module('app')
    /**
   * jQuery plugin config use ui-jq directive , config the js and css files that required
   * key: function name of the jQuery plugin
   * value: array of the css js file located
   */
  .constant('JQ_CONFIG', {
      easyPieChart:   ['/static/management/vendor/jquery/charts/easypiechart/jquery.easy-pie-chart.js'],
      sparkline:      ['/static/management/vendor/jquery/charts/sparkline/jquery.sparkline.min.js'],
      plot:           ['/static/management/vendor/jquery/charts/flot/jquery.flot.min.js',
                          '/static/management/vendor/jquery/charts/flot/jquery.flot.resize.js',
                          '/static/management/vendor/jquery/charts/flot/jquery.flot.tooltip.min.js',
                          '/static/management/vendor/jquery/charts/flot/jquery.flot.spline.js',
                          '/static/management/vendor/jquery/charts/flot/jquery.flot.orderBars.js',
                          '/static/management/vendor/jquery/charts/flot/jquery.flot.pie.min.js'],
      slimScroll:     ['/static/management/vendor/jquery/slimscroll/jquery.slimscroll.min.js'],
      sortable:       ['/static/management/vendor/jquery/sortable/jquery.sortable.js'],
      nestable:       ['/static/management/vendor/jquery/nestable/jquery.nestable.js',
                          '/static/management/vendor/jquery/nestable/nestable.css'],
      filestyle:      ['/static/management/vendor/jquery/file/bootstrap-filestyle.min.js'],
      slider:         ['/static/management/vendor/jquery/slider/bootstrap-slider.js',
                          '/static/management/vendor/jquery/slider/slider.css'],
      chosen:         ['/static/management/vendor/jquery/chosen/chosen.jquery.min.js',
                          '/static/management/vendor/jquery/chosen/chosen.css'],
      TouchSpin:      ['/static/management/vendor/jquery/spinner/jquery.bootstrap-touchspin.min.js',
                          '/static/management/vendor/jquery/spinner/jquery.bootstrap-touchspin.css'],
      wysiwyg:        ['/static/management/vendor/jquery/wysiwyg/bootstrap-wysiwyg.js',
                          '/static/management/vendor/jquery/wysiwyg/jquery.hotkeys.js'],
      dataTable:      ['/static/management/vendor/jquery/datatables/jquery.dataTables.min.js',
                          '/static/management/vendor/jquery/datatables/dataTables.bootstrap.js',
                          '/static/management/vendor/jquery/datatables/dataTables.bootstrap.css'],
      vectorMap:      ['/static/management/vendor/jquery/jvectormap/jquery-jvectormap.min.js',
                          '/static/management/vendor/jquery/jvectormap/jquery-jvectormap-world-mill-en.js',
                          '/static/management/vendor/jquery/jvectormap/jquery-jvectormap-us-aea-en.js',
                          '/static/management/vendor/jquery/jvectormap/jquery-jvectormap.css'],
      footable:       ['/static/management/vendor/jquery/footable/footable.all.min.js',
                          '/static/management/vendor/jquery/footable/footable.core.css']
      }
  )
  // oclazyload config
  .config(['$ocLazyLoadProvider', function($ocLazyLoadProvider) {
      // We configure ocLazyLoad to use the lib script.js as the async loader
      $ocLazyLoadProvider.config({
          debug:  false,
          events: true,
          modules: [
              {
                  name: 'ngGrid',
                  files: [
                      '/static/management/vendor/modules/ng-grid/ng-grid.min.js',
                      '/static/management/vendor/modules/ng-grid/ng-grid.min.css',
                      '/static/management/vendor/modules/ng-grid/theme.css'
                  ]
              },
              {
                  name: 'ui.select',
                  files: [
                      '/static/management/vendor/modules/angular-ui-select/select.min.js',
                      '/static/management/vendor/modules/angular-ui-select/select.min.css'
                  ]
              },
              {
                  name:'angularFileUpload',
                  files: [
                    '/static/management/vendor/modules/angular-file-upload/angular-file-upload.min.js'
                  ]
              },
              {
                  name:'ui.calendar',
                  files: ['/static/management/vendor/modules/angular-ui-calendar/calendar.js']
              },
              {
                  name: 'ngImgCrop',
                  files: [
                      '/static/management/vendor/modules/ngImgCrop/ng-img-crop.js',
                      '/static/management/vendor/modules/ngImgCrop/ng-img-crop.css'
                  ]
              },
              {
                  name: 'angularBootstrapNavTree',
                  files: [
                      '/static/management/vendor/modules/angular-bootstrap-nav-tree/abn_tree_directive.js',
                      '/static/management/vendor/modules/angular-bootstrap-nav-tree/abn_tree.css'
                  ]
              },
              {
                  name: 'toaster',
                  files: [
                      '/static/management/vendor/modules/angularjs-toaster/toaster.js',
                      '/static/management/vendor/modules/angularjs-toaster/toaster.css'
                  ]
              },
              {
                  name: 'textAngular',
                  files: [
                      '/static/management/vendor/modules/textAngular/textAngular-sanitize.min.js',
                      '/static/management/vendor/modules/textAngular/textAngular.min.js'
                  ]
              },
              {
                  name: 'vr.directives.slider',
                  files: [
                      '/static/management/vendor/modules/angular-slider/angular-slider.min.js',
                      '/static/management/vendor/modules/angular-slider/angular-slider.css'
                  ]
              },
              {
                  name: 'com.2fdevs.videogular',
                  files: [
                      '/static/management/vendor/modules/videogular/videogular.min.js'
                  ]
              },
              {
                  name: 'com.2fdevs.videogular.plugins.controls',
                  files: [
                      '/static/management/vendor/modules/videogular/plugins/controls.min.js'
                  ]
              },
              {
                  name: 'com.2fdevs.videogular.plugins.buffering',
                  files: [
                      '/static/management/vendor/modules/videogular/plugins/buffering.min.js'
                  ]
              },
              {
                  name: 'com.2fdevs.videogular.plugins.overlayplay',
                  files: [
                      '/static/management/vendor/modules/videogular/plugins/overlay-play.min.js'
                  ]
              },
              {
                  name: 'com.2fdevs.videogular.plugins.poster',
                  files: [
                      '/static/management/vendor/modules/videogular/plugins/poster.min.js'
                  ]
              },
              {
                  name: 'com.2fdevs.videogular.plugins.imaads',
                  files: [
                      '/static/management/vendor/modules/videogular/plugins/ima-ads.min.js'
                  ]
              }
          ]
      });
  }])
;