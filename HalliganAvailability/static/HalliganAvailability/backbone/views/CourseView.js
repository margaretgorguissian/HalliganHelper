app = typeof app !== "undefined" ? app : {};

app.CourseView = Backbone.View.extend({
    el: '#content',
    initialize: function( options ) {
        this.coursePk = options.coursePk;
        this.course = new app.Course( options, {} );
        this.listenTo( this.course, "change", this.render );
        this.course.fetch( {reset: true} );
    },
    template: _.template( $('#courseLayoutTemplate').html() ),
    render: function() {
        this.$el.html( this.template( this.course.toJSON() ) );
        new app.queueItemsView( { el: this.$( '#queueContent' ),
                                  collection: this.course.requests,
                                  course: this.course
                                } );
        new app.OfficeHoursView( { el: this.$( '#officeHourContent' ),
                                  collection: this.course.officeHours,
                                  course: this.course
                                } );
    },
    handleUpdate: function( update ) {
        switch( update.type ) {
            case 'office_hour_update':
            case 'office_hour_create':
                this.course.handleOfficeHour( update );
                break;
            case 'request_update':
            case 'request_create':
                this.course.handleRequest( update );
                break;
        } 
    }
});