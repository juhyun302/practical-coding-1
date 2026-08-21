package com.example.demo.entity;
import com.example.demo.constant.ItemSellStatus;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import java.time.LocalDateTime;
import jakarta.persistence.*;
import org.springframework.stereotype.Component;

@Table(name="item")
@Getter
@Setter
@ToString
@Entity
public class Item {

    @Id
    @Column(name="item_id")
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id; //상품 코드

    @Column(nullable = false, length= 50)
    private String itemNm; // 상품 이름

    @Column(name="price", nullable = false)
    private int price; // 상품 가격

    @Column(nullable = false)
    private int stockNumber; // 제고 수량

    @Lob
    @Column(nullable = false)
    private String itemDetail; // 상품 상세 가격

    @Enumerated(EnumType.STRING)
    private ItemSellStatus itemSellStatus; // 상품 판매 상태

    private LocalDateTime regTime; // 등록 시간
    private LocalDateTime updateTime; // 수정 시간
}
