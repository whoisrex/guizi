'use strict';

/**
 * Config for the router
 */
angular.module('app')
  .run(
    [          '$rootScope', '$state', '$stateParams',
      function ($rootScope,   $state,   $stateParams) {
          $rootScope.$state = $state;
          $rootScope.$stateParams = $stateParams;        
      }
    ]
  )
  .config(
    [          '$stateProvider', '$urlRouterProvider',
      function ($stateProvider,   $urlRouterProvider) {
          
          $urlRouterProvider
              .otherwise('/app/dashboard-v1');
          $stateProvider
              .state('app', {
                  abstract: true,
                  url: '/app',
                  templateUrl: '/static/management/tpl/app.html'
              })
              .state('app.dashboard-v1', {
                  url: '/dashboard-v1',
                  templateUrl: '/static/management/tpl/app_dashboard_v1.html',
                  resolve: {
                    deps: ['$ocLazyLoad',
                      function( $ocLazyLoad ){
                        return $ocLazyLoad.load(['/static/management/js/controllers/chart.js']);
                    }]
                  }
              })
              .state('app.dashboard-v2', {
                  url: '/dashboard-v2',
                  templateUrl: '/management/tpl/app_dashboard_v2.html',
                  resolve: {
                    deps: ['$ocLazyLoad',
                      function( $ocLazyLoad ){
                        return $ocLazyLoad.load(['/static/management/js/controllers/chart.js']);
                    }]
                  }
              })
              .state('app.manage', {
                  url: '/manage',
                  template: '<div ui-view></div>',
                  resolve: {
                    deps: ['$ocLazyLoad',
                      function( $ocLazyLoad ){
                          return $ocLazyLoad.load('/static/management/vendor/libs/moment.min.js').then(
                              function(){
                                return $ocLazyLoad.load('/static/management/js/controllers/manage.js');
                              }
                          );
                    }]
                  }
              })
              .state('app.manage.users', {
                  url:'/users',
                  templateUrl: '/static/management/tpl/manage_users.html'
              })
              .state('app.manage.groups', {
                  url:'/users',
                  templateUrl: '/static/management/tpl/manage_users.html'
              })
              .state('app.front', {
                  url: '/front',
                  template: '<div ui-view class="fade-in-up"></div>',
                  resolve: {
                    deps: ['$ocLazyLoad',
                      function( $ocLazyLoad ){
                          return $ocLazyLoad.load('/static/management/vendor/libs/moment.min.js').then(
                              function() {
                                return $ocLazyLoad.load(['/static/management/js/controllers/front.js']);
                              }
                          )
                    }]
                  }
              })
              .state('app.front.brands', {
                  url:'/brands',
                  templateUrl: '/static/management/tpl/front_brand.html'
              })
              .state('app.front.new-brand', {
                  url:'/new-brand',
                  templateUrl: '/static/management/tpl/front_new_brand.html',
                  resolve: {
                      deps: ['$ocLazyLoad',
                          function( $ocLazyLoad ){
                              return $ocLazyLoad.load('textAngular').then(
                                  function(){
                                     return $ocLazyLoad.load('angularFileUpload').then(
                                         function() {
                                             return $ocLazyLoad.load("ngImgCrop").then(
                                                 function(){
                                                    return $ocLazyLoad.load("/static/management/js/controllers/file-upload.js");
                                             });
                                     });
                                  }
                              );
                          }
                      ]
                  }
              })
              .state('app.front.products', {
                  url:'/products',
                  templateUrl: '/static/management/tpl/front_product.html'
              })
              .state('app.front.spaces', {
                  url:'/spaces',
                  templateUrl: '/static/management/tpl/front_space.html'
              })
              .state('app.front.new-space', {
                  url: '/new-space',
                  templateUrl: '/static/management/tpl/front_new_space.html'
              })
              .state('app.front.articles', {
                  url:'/articles',
                  templateUrl: '/static/management/tpl/front_article.html'
              })
              .state('app.front.images', {
                  url:'/images',
                  templateUrl: '/static/management/tpl/front_image.html'
              })
              .state('app.ui', {
                  url: '/ui',
                  template: '<div ui-view class="fade-in-up"></div>'
              })
              .state('app.ui.buttons', {
                  url: '/buttons',
                  templateUrl: '/static/management/tpl/ui_buttons.html'
              })
              .state('app.ui.icons', {
                  url: '/icons',
                  templateUrl: '/static/management/tpl/ui_icons.html'
              })
              .state('app.ui.grid', {
                  url: '/grid',
                  templateUrl: '/static/management/tpl/ui_grid.html'
              })
              .state('app.ui.widgets', {
                  url: '/widgets',
                  templateUrl: '/static/management/tpl/ui_widgets.html'
              })          
              .state('app.ui.bootstrap', {
                  url: '/bootstrap',
                  templateUrl: '/static/management/tpl/ui_bootstrap.html'
              })
              .state('app.ui.sortable', {
                  url: '/sortable',
                  templateUrl: '/static/management/tpl/ui_sortable.html'
              })
              .state('app.ui.portlet', {
                  url: '/portlet',
                  templateUrl: '/static/management/tpl/ui_portlet.html'
              })
              .state('app.ui.timeline', {
                  url: '/timeline',
                  templateUrl: '/static/management/tpl/ui_timeline.html'
              })
              .state('app.ui.tree', {
                  url: '/tree',
                  templateUrl: '/static/management/tpl/ui_tree.html',
                  resolve: {
                      deps: ['$ocLazyLoad',
                        function( $ocLazyLoad ){
                          return $ocLazyLoad.load('angularBootstrapNavTree').then(
                              function(){
                                 return $ocLazyLoad.load('/static/management/js/controllers/tree.js');
                              }
                          );
                        }
                      ]
                  }
              })
              .state('app.ui.toaster', {
                  url: '/toaster',
                  templateUrl: '/static/management/tpl/ui_toaster.html',
                  resolve: {
                      deps: ['$ocLazyLoad',
                        function( $ocLazyLoad){
                          return $ocLazyLoad.load('toaster').then(
                              function(){
                                 return $ocLazyLoad.load('/static/management/js/controllers/toaster.js');
                              }
                          );
                      }]
                  }
              })
              .state('app.ui.jvectormap', {
                  url: '/jvectormap',
                  templateUrl: '/static/management/tpl/ui_jvectormap.html',
                  resolve: {
                      deps: ['$ocLazyLoad',
                        function( $ocLazyLoad){
                          return $ocLazyLoad.load('/static/management/js/controllers/vectormap.js');
                      }]
                  }
              })
              .state('app.ui.googlemap', {
                  url: '/googlemap',
                  templateUrl: '/static/management/tpl/ui_googlemap.html',
                  resolve: {
                      deps: ['uiLoad',
                        function( uiLoad ){
                          return uiLoad.load( [
                            '/static/management/js/app/map/load-google-maps.js',
                            '/static/management/js/app/map/ui-map.js',
                            '/static/management/js/app/map/map.js'] ).then(
                              function(){
                                return loadGoogleMaps(); 
                              }
                            );
                      }]
                  }
              })
              .state('app.chart', {
                  url: '/chart',
                  templateUrl: 'tpl/ui_chart.html',
                  resolve: {
                      deps: ['uiLoad',
                        function( uiLoad){
                          return uiLoad.load('/static/management/js/controllers/chart.js');
                      }]
                  }
              })
              // table
              .state('app.table', {
                  url: '/table',
                  template: '<div ui-view></div>'
              })
              .state('app.table.static', {
                  url: '/static',
                  templateUrl: '/static/management/tpl/table_static.html'
              })
              .state('app.table.datatable', {
                  url: '/datatable',
                  templateUrl: '/static/management/tpl/table_datatable.html'
              })
              .state('app.table.footable', {
                  url: '/footable',
                  templateUrl: '/static/management/tpl/table_footable.html'
              })
              .state('app.table.grid', {
                  url: '/grid',
                  templateUrl: '/static/management/tpl/table_grid.html',
                  resolve: {
                      deps: ['$ocLazyLoad',
                        function( $ocLazyLoad ){
                          return $ocLazyLoad.load('ngGrid').then(
                              function(){
                                  return $ocLazyLoad.load('/static/management/js/controllers/grid.js');
                              }
                          );
                      }]
                  }
              })
              // form
              .state('app.form', {
                  url: '/form',
                  template: '<div ui-view class="fade-in"></div>',
                  resolve: {
                      deps: ['uiLoad',
                        function( uiLoad){
                          return uiLoad.load('/static/management/js/controllers/form.js');
                      }]
                  }
              })
              .state('app.form.elements', {
                  url: '/elements',
                  templateUrl: '/static/management/tpl/form_elements.html'
              })
              .state('app.form.validation', {
                  url: '/validation',
                  templateUrl: '/static/management/tpl/form_validation.html'
              })
              .state('app.form.wizard', {
                  url: '/wizard',
                  templateUrl: '/static/management/tpl/form_wizard.html'
              })
              .state('app.form.fileupload', {
                  url: '/fileupload',
                  templateUrl: '/static/management/tpl/form_fileupload.html',
                  resolve: {
                      deps: ['$ocLazyLoad',
                        function( $ocLazyLoad){
                          return $ocLazyLoad.load('angularFileUpload').then(
                              function(){
                                 return $ocLazyLoad.load('/static/management/js/controllers/file-upload.js');
                              }
                          );
                      }]
                  }
              })
              .state('app.form.imagecrop', {
                  url: '/imagecrop',
                  templateUrl: '/static/management/tpl/form_imagecrop.html',
                  resolve: {
                      deps: ['$ocLazyLoad',
                        function( $ocLazyLoad){
                          return $ocLazyLoad.load('ngImgCrop').then(
                              function(){
                                 return $ocLazyLoad.load('/static/management/js/controllers/imgcrop.js');
                              }
                          );
                      }]
                  }
              })
              .state('app.form.select', {
                  url: '/select',
                  templateUrl: '/static/management/tpl/form_select.html',
                  controller: 'SelectCtrl',
                  resolve: {
                      deps: ['$ocLazyLoad',
                        function( $ocLazyLoad ){
                          return $ocLazyLoad.load('ui.select').then(
                              function(){
                                  return $ocLazyLoad.load('/static/management/js/controllers/select.js');
                              }
                          );
                      }]
                  }
              })
              .state('app.form.slider', {
                  url: '/slider',
                  templateUrl: '/static/management/tpl/form_slider.html',
                  controller: 'SliderCtrl',
                  resolve: {
                      deps: ['$ocLazyLoad',
                        function( $ocLazyLoad ){
                          return $ocLazyLoad.load('vr.directives.slider').then(
                              function(){
                                  return $ocLazyLoad.load('/static/management/js/controllers/slider.js');
                              }
                          );
                      }]
                  }
              })
              .state('app.form.editor', {
                  url: '/editor',
                  templateUrl: '/static/management/tpl/form_editor.html',
                  controller: 'EditorCtrl',
                  resolve: {
                      deps: ['$ocLazyLoad',
                        function( $ocLazyLoad ){
                          return $ocLazyLoad.load('textAngular').then(
                              function(){
                                  return $ocLazyLoad.load('/static/management/js/controllers/editor.js');
                              }
                          );
                      }]
                  }
              })
              // pages
              .state('app.page', {
                  url: '/page',
                  template: '<div ui-view class="fade-in-down"></div>'
              })
              .state('app.page.profile', {
                  url: '/profile',
                  templateUrl: '/static/management/tpl/page_profile.html'
              })
              .state('app.page.post', {
                  url: '/post',
                  templateUrl: '/static/management/tpl/page_post.html'
              })
              .state('app.page.search', {
                  url: '/search',
                  templateUrl: '/static/management/tpl/page_search.html'
              })
              .state('app.page.invoice', {
                  url: '/invoice',
                  templateUrl: '/static/management/tpl/page_invoice.html'
              })
              .state('app.page.price', {
                  url: '/price',
                  templateUrl: '/static/management/tpl/page_price.html'
              })
              .state('app.docs', {
                  url: '/docs',
                  templateUrl: '/static/management/tpl/docs.html'
              })
              // others
              .state('lockme', {
                  url: '/lockme',
                  templateUrl: '/static/management/tpl/page_lockme.html'
              })
              .state('access', {
                  url: '/access',
                  template: '<div ui-view class="fade-in-right-big smooth"></div>'
              })
              .state('access.signin', {
                  url: '/signin',
                  templateUrl: '/static/management/tpl/page_signin.html',
                  resolve: {
                      deps: ['uiLoad',
                        function( uiLoad ){
                          return uiLoad.load( ['/static/management/js/controllers/signin.js'] );
                      }]
                  }
              })
              .state('access.signup', {
                  url: '/signup',
                  templateUrl: '/static/management/tpl/page_signup.html',
                  resolve: {
                      deps: ['uiLoad',
                        function( uiLoad ){
                          return uiLoad.load( ['/static/management/js/controllers/signup.js'] );
                      }]
                  }
              })
              .state('access.forgotpwd', {
                  url: '/forgotpwd',
                  templateUrl: '/static/management/tpl/page_forgotpwd.html'
              })
              .state('access.404', {
                  url: '/404',
                  templateUrl: '/static/management/tpl/page_404.html'
              })

              // fullCalendar
              .state('app.calendar', {
                  url: '/calendar',
                  templateUrl: '/static/management/tpl/app_calendar.html',
                  // use resolve to load other dependences
                  resolve: {
                      deps: ['$ocLazyLoad', 'uiLoad',
                        function( $ocLazyLoad, uiLoad ){
                          return uiLoad.load(
                            ['/static/management/vendor/jquery/fullcalendar/fullcalendar.css',
                              '/static/management/vendor/jquery/fullcalendar/theme.css',
                              '/static/management/vendor/jquery/jquery-ui-1.10.3.custom.min.js',
                              '/static/management/vendor/libs/moment.min.js',
                              '/static/management/vendor/jquery/fullcalendar/fullcalendar.min.js',
                              '/static/management/js/app/calendar/calendar.js']
                          ).then(
                            function(){
                              return $ocLazyLoad.load('ui.calendar');
                            }
                          )
                      }]
                  }
              })

              // mail
              .state('app.mail', {
                  abstract: true,
                  url: '/mail',
                  templateUrl: '/static/management/tpl/mail.html',
                  // use resolve to load other dependences
                  resolve: {
                      deps: ['uiLoad',
                        function( uiLoad ){
                          return uiLoad.load( ['/static/management/js/app/mail/mail.js',
                                               '/static/management/js/app/mail/mail-service.js',
                                               '/static/management/vendor/libs/moment.min.js'] );
                      }]
                  }
              })
              .state('app.mail.list', {
                  url: '/inbox/{fold}',
                  templateUrl: '/static/management/tpl/mail.list.html'
              })
              .state('app.mail.detail', {
                  url: '/{mailId:[0-9]{1,4}}',
                  templateUrl: '/static/management/tpl/mail.detail.html'
              })
              .state('app.mail.compose', {
                  url: '/compose',
                  templateUrl: '/static/management/tpl/mail.new.html'
              })

              .state('layout', {
                  abstract: true,
                  url: '/layout',
                  templateUrl: '/static/management/tpl/layout.html'
              })
              .state('layout.fullwidth', {
                  url: '/fullwidth',
                  views: {
                      '': {
                          templateUrl: '/static/management/tpl/layout_fullwidth.html'
                      },
                      'footer': {
                          templateUrl: '/static/management/tpl/layout_footer_fullwidth.html'
                      }
                  },
                  resolve: {
                      deps: ['uiLoad',
                        function( uiLoad ){
                          return uiLoad.load( ['/static/management/js/controllers/vectormap.js'] );
                      }]
                  }
              })
              .state('layout.mobile', {
                  url: '/mobile',
                  views: {
                      '': {
                          templateUrl: '/static/management/tpl/layout_mobile.html'
                      },
                      'footer': {
                          templateUrl: '/static/management/tpl/layout_footer_mobile.html'
                      }
                  }
              })
              .state('layout.app', {
                  url: '/app',
                  views: {
                      '': {
                          templateUrl: '/static/management/tpl/layout_app.html'
                      },
                      'footer': {
                          templateUrl: '/static/management/tpl/layout_footer_fullwidth.html'
                      }
                  },
                  resolve: {
                      deps: ['uiLoad',
                        function( uiLoad ){
                          return uiLoad.load( ['/static/management/js/controllers/tab.js'] );
                      }]
                  }
              })
              .state('apps', {
                  abstract: true,
                  url: '/apps',
                  templateUrl: '/static/management/tpl/layout.html'
              })
              .state('apps.note', {
                  url: '/note',
                  templateUrl: '/static/management/tpl/apps_note.html',
                  resolve: {
                      deps: ['uiLoad',
                        function( uiLoad ){
                          return uiLoad.load( ['/static/management/js/app/note/note.js',
                                               '/static/management/vendor/libs/moment.min.js'] );
                      }]
                  }
              })
              .state('apps.contact', {
                  url: '/contact',
                  templateUrl: '/static/management/tpl/apps_contact.html',
                  resolve: {
                      deps: ['uiLoad',
                        function( uiLoad ){
                          return uiLoad.load( ['/static/management/js/app/contact/contact.js'] );
                      }]
                  }
              })
              .state('app.weather', {
                  url: '/weather',
                  templateUrl: '/static/management/tpl/apps_weather.html',
                  resolve: {
                      deps: ['$ocLazyLoad',
                        function( $ocLazyLoad ){
                          return $ocLazyLoad.load(
                              {
                                  name: 'angular-skycons',
                                  files: ['/static/management/js/app/weather/skycons.js',
                                          '/static/management/vendor/libs/moment.min.js',
                                          '/static/management/js/app/weather/angular-skycons.js',
                                          '/static/management/js/app/weather/ctrl.js' ]
                              }
                          );
                      }]
                  }
              })
              .state('music', {
                  url: '/music',
                  templateUrl: '/static/management/tpl/music.html',
                  controller: 'MusicCtrl',
                  resolve: {
                      deps: ['$ocLazyLoad',
                        function( $ocLazyLoad ){
                          return $ocLazyLoad.load([
                            'com.2fdevs.videogular', 
                            'com.2fdevs.videogular.plugins.controls', 
                            'com.2fdevs.videogular.plugins.overlayplay',
                            'com.2fdevs.videogular.plugins.poster',
                            'com.2fdevs.videogular.plugins.buffering',
                            '/static/management/js/app/music/ctrl.js',
                            '/static/management/js/app/music/theme.css'
                          ]);
                      }]
                  }
              })
                .state('music.home', {
                    url: '/home',
                    templateUrl: '/static/management/tpl/music.home.html'
                })
                .state('music.genres', {
                    url: '/genres',
                    templateUrl: '/static/management/tpl/music.genres.html'
                })
                .state('music.detail', {
                    url: '/detail',
                    templateUrl: '/static/management/tpl/music.detail.html'
                })
                .state('music.mtv', {
                    url: '/mtv',
                    templateUrl: '/static/management/tpl/music.mtv.html'
                })
                .state('music.mtvdetail', {
                    url: '/mtvdetail',
                    templateUrl: '/static/management/tpl/music.mtv.detail.html'
                })
                .state('music.playlist', {
                    url: '/playlist/{fold}',
                    templateUrl: '/static/management/tpl/music.playlist.html'
                })
      }
    ]
  );