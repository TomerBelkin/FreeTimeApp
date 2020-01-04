import { Song } from './../models/song';
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';




@Injectable({
  providedIn: 'root'
})
export class SongService {
  private url = "http://localhost:5000/song"

  constructor(private http: HttpClient) { 

  }

  getSongs(): Observable<Song[]>{
    return this.http.get<Song[]>(this.url);
  }

  getSong(id: number): Observable<Song>{
    return this.http.get<Song>(this.url + '/' + id);
  }

  downloadSongs(songs: String){
    return this.http.post("http://localhost:5000/song/download", songs).subscribe(response => console.log(response));
  }
}
