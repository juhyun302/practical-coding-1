package com.ajou.prcoding.myweb.service;

import com.ajou.prcoding.myweb.dto.FavoriteMusicRequestDto;
import com.ajou.prcoding.myweb.dto.MusicList;
import com.ajou.prcoding.myweb.entity.FavoriteMusic;
import com.ajou.prcoding.myweb.repository.FavoriteRepository;
import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.client.RestTemplate;

import java.util.List;

@Service
@Transactional
@RequiredArgsConstructor
public class MusicService {

    private final FavoriteRepository albumsRepo;
    RestTemplate restTemplate = new RestTemplate();

    public MusicList searchMusic(String term) {
        try {
            String response = restTemplate.getForObject("https://itunes.apple.com/search?term={term}&entity={entity}", String.class, term, "album");
            ObjectMapper mapper = new ObjectMapper();
            return mapper.readValue(response, MusicList.class);
        } catch(Exception e) {
            System.out.println(e.toString());
            return null;
        }
    }

    public List<FavoriteMusic> getLikes() {
        try {
            return albumsRepo.findAll();
        } catch (Exception e) {
            System.out.println(e.toString());
            return null;
        }
    }

    public int saveFavorite(FavoriteMusicRequestDto favorite) {
        FavoriteMusic music = albumsRepo.save(favorite.toEntity());
        if(music != null) {
            return 1;
        } else {
            return 0;
        }
    }

    public int deleteFavorite(String id) {
        try {
            albumsRepo.deleteById(id);
            return 1;
        } catch (Exception e) {
            System.out.println("삭제 실패 (잘못된 ID): " + e.toString());
            return 0;
        }
    }
}
