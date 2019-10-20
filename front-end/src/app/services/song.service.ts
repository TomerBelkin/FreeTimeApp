import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class SongService {
  private url = "http://localhost:5000/song/"

  constructor(private http: HttpClient) { 

  }

  getSongs(){
    return this.http.get(this.url);
  }
}
