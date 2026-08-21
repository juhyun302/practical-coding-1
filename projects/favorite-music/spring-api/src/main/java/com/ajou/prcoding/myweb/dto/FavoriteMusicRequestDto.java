package com.ajou.prcoding.myweb.dto;

import com.ajou.prcoding.myweb.entity.FavoriteMusic;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@ToString
public class FavoriteMusicRequestDto {

    // 15쪽 Entity에 있던 필드들 똑같이 선언 (어노테이션은 빼고!) [cite: 196]
    private String collectionId;
    private String collectionType;
    private String artistId;
    private String artistName;
    private String artistViewUrl;
    private String collectionName;
    private String collectionViewUrl;

    // DTO를 Entity로 변환해주는 메서드 완성하기 [cite: 204]
    public FavoriteMusic toEntity() {
        FavoriteMusic music = new FavoriteMusic();
        music.setCollectionId(this.collectionId);
        music.setCollectionType(this.collectionType);
        music.setArtistId(this.artistId);
        music.setArtistName(this.artistName);
        music.setArtistViewUrl(this.artistViewUrl);
        music.setCollectionName(this.collectionName);
        music.setCollectionViewUrl(this.collectionViewUrl);
        return music;
    }
}
