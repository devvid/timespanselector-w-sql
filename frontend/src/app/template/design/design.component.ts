import { OnInit, Injectable } from '@angular/core';
import {NgbDate, NgbCalendar} from '@ng-bootstrap/ng-bootstrap';

import { ApiService } from "../../service/api.service";
import { Post, PostHistory } from "../../service/types";
import { strict } from 'assert';

export class DesignComponent implements OnInit {

  fromDate: NgbDate;
  toDate: NgbDate | null = null;
  hoveredDate: NgbDate | null = null;

  fromtime;
  totime;

  selectedPost: string = '1';
  posts: Post[];
  history: PostHistory[];

  error: string;

  constructor(
    public calendar: NgbCalendar,
    private api: ApiService
  ) { }

  ngOnInit(): void {
    this.getAllPost();
  }

  /**
   * Get all posts to complete form
   */
  getAllPost(){
    this.api.allPosts().catch(err => {
      console.error("All Posts Error")
    }).then(response => {
      this.posts = response['posts'];
    })
  }

  /**
   * On button press.
   */
  search() {

    if (this.toDate == null && this.fromDate == null ) return this.error = "Please select a date range";
    if (this.totime == undefined ) return this.error = "Please select a ending time";
    if (this.fromtime == undefined ) return this.error = "Please select a starting time";

    console.log("Test", this.selectedPost)
    console.log(this.selectedPost)
    console.log(this.fromDate)
    console.log(this.toDate)
    console.log(this.fromtime)
    console.log(this.totime)

    var inputdate = {
      id: this.selectedPost,
      date_time_to: new Date(Date.UTC(this.toDate.year, this.toDate.month, this.toDate.day, this.totime.hour, this.totime.minute, this.totime.second)),
      date_time_from: new Date(Date.UTC(this.fromDate.year, this.fromDate.month, this.fromDate.day, this.fromtime.hour, this.fromtime.minute, this.fromtime.second)),
    }
    this.api.searchQuery(inputdate).catch(err=>{
      console.error("Search Query Error")
      this.error = "Woops, some thing went wrong with the query"
    }).then(response => {
      this.history = response['history'];
    })
    this.error = ""
  }

}
