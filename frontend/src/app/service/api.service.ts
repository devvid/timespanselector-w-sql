import { Injectable, OnInit, OnDestroy } from '@angular/core';
import { Observable, Subscription } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Post } from './types';

type Query = {
  posts: Post[]
}

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  result: Post[];

  constructor(
    private http: HttpClient
  ) { }

  allPosts(){
    return this.http.get('http://localhost:5000/api/post/all').toPromise()
  }

  searchQuery(data) {
    return this.http.post<Query>('http://localhost:5000/api/post-history/search', data).toPromise()
  }

}
